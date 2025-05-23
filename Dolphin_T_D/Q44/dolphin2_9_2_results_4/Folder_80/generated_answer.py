def composite_nums_between_indices(nums):

    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return True
        return False
    return {nums[i] for i in range(62, 79) if is_composite(nums[i])}