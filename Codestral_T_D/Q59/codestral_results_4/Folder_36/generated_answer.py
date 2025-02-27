def all_left_truncatable_prime(nums):
    x = nums[992]

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

    def truncate_left(n):
        return [int(str(n)[i:]) for i in range(1, len(str(n)))]

    def is_left_truncatable_prime(n):
        if not is_prime(n):
            return False
        for t in truncate_left(n):
            if not is_prime(t):
                return False
        return True
    return sorted([i for i in range(2, x) if is_left_truncatable_prime(i)])