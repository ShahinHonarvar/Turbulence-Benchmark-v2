def all_left_right_truncatable_prime(nums):
    x = nums[100]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        while n > 9:
            if not is_prime(n):
                return False
            n //= 10
            if not is_prime(n):
                return False
        return is_prime(n)
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)