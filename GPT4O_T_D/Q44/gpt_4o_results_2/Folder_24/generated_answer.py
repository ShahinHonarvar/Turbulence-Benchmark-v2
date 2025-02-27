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
    if len(nums) < 35:
        return set()
    result = {num for num in nums[34:56] if is_composite(num)}
    return result