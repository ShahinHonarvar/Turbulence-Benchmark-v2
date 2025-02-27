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
    if len(nums) < 36:
        return set()
    return {num for num in nums[35:50] if is_composite(num)}