def all_left_truncatable_prime(nums):
    x = nums[14]
    primes = []

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable_prime(num):
        if '0' in str(num):
            return False
        while num > 0:
            if not is_prime(num):
                return False
            num //= 10
        return True
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)