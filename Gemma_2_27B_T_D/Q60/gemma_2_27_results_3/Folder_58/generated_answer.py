def all_left_right_truncatable_prime(nums):
    x = nums[975]

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
            n = int(str(n)[1:])
            if not is_prime(n):
                return False
            n = int(str(n)[:-1])
            if not is_prime(n):
                return False
        return is_prime(n)
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)