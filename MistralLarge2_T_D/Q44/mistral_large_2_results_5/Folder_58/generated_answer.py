def composite_nums_between_indices(nums):

    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    result_set = set()
    for i in range(533, 606):
        if 0 <= i < len(nums) and is_composite(nums[i]):
            result_set.add(nums[i])
    return result_set