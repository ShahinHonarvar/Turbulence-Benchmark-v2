def all_left_right_truncatable_prime(nums):
    x = nums[49]
    left_truncatable_primes = []
    right_truncatable_primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        if not is_prime(n):
            return False
        return is_left_truncatable_prime(int(str(n)[1:]))

    def is_right_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        if not is_prime(n):
            return False
        return is_right_truncatable_prime(int(str(n)[:-1]))
    for i in range(2, x + 1):
        if '0' not in str(i):
            if is_left_truncatable_prime(i) and is_right_truncatable_prime(i):
                left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)