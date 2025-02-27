def all_left_right_truncatable_prime(nums):
    x = nums[54]

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

    def truncate(n):
        res = []
        while n > 0:
            n = n // 10
            res.append(n)
            res.append(int(str(n)[1:]))
        return res

    def is_left_right_truncatable_prime(n):
        return all((is_prime(i) for i in truncate(n)))
    return sorted([i for i in range(2, x + 1) if is_left_right_truncatable_prime(i)], reverse=True)