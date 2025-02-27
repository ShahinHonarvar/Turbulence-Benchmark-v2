def all_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = nums[41]
    right_truncatable_primes = []
    for num in range(2, x):
        is_truncatable_prime = True
        num_str = str(num)
        for i in range(len(num_str)):
            if not is_prime(int(num_str[:-i - 1])):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)