def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncated_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = n // 10
        return True

    def is_right_truncated_prime(n):
        s = str(n)
        while len(s) > 0:
            if not is_prime(int(s)):
                return False
            s = s[:-1]
        return True

    def is_left_right_truncated_prime(n):
        if '0' in str(n):
            return False
        return is_left_truncated_prime(n) and is_right_truncated_prime(n)
    x = nums[39]
    left_right_truncatable_primes = []
    for n in range(2, x + 1):
        if is_left_right_truncated_prime(n):
            left_right_truncatable_primes.append(n)
    return sorted(left_right_truncatable_primes, reverse=True)