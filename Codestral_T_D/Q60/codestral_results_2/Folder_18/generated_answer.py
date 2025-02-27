def all_left_right_truncatable_prime(nums):

    def is_truncatable_prime(n):
        if n < 2:
            return False
        if n in (2, 3, 5, 7):
            return True
        if '0' in str(n) or n % 2 == 0:
            return False
        r = n
        while r > 0:
            if not is_prime(r):
                return False
            r = r // 10
        l = n
        while l > 9:
            l = int(str(l)[1:])
            if not is_prime(l):
                return False
        return True

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    x = nums[429]
    truncatable_primes = [n for n in range(x, 1, -1) if is_truncatable_prime(n)]
    return sorted(truncatable_primes, reverse=True)