def all_left_truncatable_prime(nums):

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

    def left_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        elif not is_prime(n) or '0' in str(n):
            return False
        else:
            return left_truncatable_prime(int(str(n)[1:]))
    x = nums[645]
    return sorted([n for n in range(2, x) if left_truncatable_prime(n)])