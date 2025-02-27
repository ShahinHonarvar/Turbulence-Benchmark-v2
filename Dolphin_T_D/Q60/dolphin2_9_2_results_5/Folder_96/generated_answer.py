def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n in (2, 3):
            return True
        if n % 2 == 0 or n == 1:
            return False
        ii = 3
        while ii * ii <= n:
            if n % ii == 0:
                return False
            ii += 2
        return True

    def is_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        if n % 10 == 0:
            return False
        m, x = divmod(n, 10)
        while m > 0:
            if not is_prime(m):
                return False
            m, x = divmod(m, 10)
        if not is_prime(x):
            return False
        return True
    nums = list(nums)
    nums.sort()
    return [i for i in nums if is_truncatable_prime(i)]