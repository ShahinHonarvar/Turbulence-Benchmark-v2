def composite_nums_between_indices(nums):

    def is_composite(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return True
        return False
    return {x for x in nums[10:67] if is_composite(x)}