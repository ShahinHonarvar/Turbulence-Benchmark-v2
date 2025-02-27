def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2 or '0' in str(n):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n >= 10:
            n = int(str(n)[1:])
            if not is_prime(n):
                return False
        return True

    def is_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n >= 10:
            n = int(str(n)[:-1])
            if not is_prime(n):
                return False
        return True
    x = nums[71]
    left_right_truncatable_primes = []
    for n in range(2, x + 1):
        if is_left_truncatable_prime(n) and is_right_truncatable_prime(n):
            left_right_truncatable_primes.append(n)
    return sorted(left_right_truncatable_primes, reverse=True)