def all_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = nums[67]
    right_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            num_str = str(i)
            for j in range(len(num_str)):
                if not is_prime(int(num_str[:-j - 1])):
                    break
            else:
                right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)