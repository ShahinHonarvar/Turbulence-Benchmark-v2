def all_left_right_truncatable_prime(nums):
    x = nums[91]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def truncate_left(n):
        return int(str(n)[1:])

    def truncate_right(n):
        return int(str(n)[:-1])

    def is_left_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = truncate_left(n)
        return True

    def is_right_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = truncate_right(n)
        return True
    for n in range(2, x + 1):
        if '0' not in str(n) and is_left_truncatable_prime(n) and is_right_truncatable_prime(n):
            primes.append(n)
    return sorted(primes)