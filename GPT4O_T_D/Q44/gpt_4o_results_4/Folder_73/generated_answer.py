def composite_nums_between_indices(nums):

    def is_composite(n):
        if n <= 1:
            return False
        if n <= 3:
            return False
        if n % 2 == 0 or n % 3 == 0:
            return True
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return True
            i += 6
        return False
    return {n for n in nums[28:41] if is_composite(n)}