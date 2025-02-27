def all_left_truncatable_prime(nums):
    x = nums[100]

    def is_prime(n):
        if n < 2:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        w = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += w
            w = 6 - w
        return True

    def left_truncatable_prime(n):
        if not '0' in str(n) and is_prime(n):
            while n > 0:
                n //= 10
                if n > 0 and (not is_prime(n)):
                    return False
            return True
        return False
    return sorted(filter(left_truncatable_prime, range(x)))