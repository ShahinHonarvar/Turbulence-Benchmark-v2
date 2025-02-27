def composite_nums_between_indices(nums):

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    start_index, end_index = (64, 66)
    return {num for num in nums[start_index:end_index + 1] if is_composite(num)}