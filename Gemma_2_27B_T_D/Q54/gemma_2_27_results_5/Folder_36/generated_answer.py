def all_right_truncatable_prime(nums):
    x = nums[992]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(2, x):
        if is_prime(i):
            right_truncatable = True
            num_str = str(i)
            for j in range(1, len(num_str)):
                if not is_prime(int(num_str[:-j])):
                    right_truncatable = False
                    break
            if right_truncatable:
                primes.append(i)
    return sorted(primes)