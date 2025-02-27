def composite_nums_between_indices(nums):

    def is_composite(n):
        if n > 1:
            for i in range(2, n):
                if n % i == 0:
                    return True
            return False
        return False
    return {nums[i] for i in range(25, 60) if is_composite(nums[i])}