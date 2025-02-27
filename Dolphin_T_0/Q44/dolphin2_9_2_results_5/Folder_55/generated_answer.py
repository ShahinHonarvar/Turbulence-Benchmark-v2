def composite_nums_between_indices(nums):

    def is_composite(x):
        if x < 2:
            return False
        for i in range(2, x):
            if x % i == 0:
                return True
        return False
    return {num for num in nums[10:101] if is_composite(num)}