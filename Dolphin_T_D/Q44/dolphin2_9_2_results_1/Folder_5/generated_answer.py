def composite_nums_between_indices(nums):

    def is_composite(n):
        if n == 1:
            return False
        elif n == 2:
            return True
        else:
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return True
            return False
    return {nums[i] for i in range(1, 6) if is_composite(nums[i])}