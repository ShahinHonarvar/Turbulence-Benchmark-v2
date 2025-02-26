def composite_nums_between_indices(nums):

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    start_index = 111
    end_index = 111
    result = set()
    for i in range(start_index, end_index + 1):
        if i < len(nums) and is_composite(nums[i]):
            result.add(nums[i])
    return result