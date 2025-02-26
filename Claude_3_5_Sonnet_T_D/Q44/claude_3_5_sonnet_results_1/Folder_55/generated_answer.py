def composite_nums_between_indices(nums):

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    start_index = 10
    end_index = 100
    result = set()
    for i in range(start_index, min(end_index + 1, len(nums))):
        if is_composite(nums[i]):
            result.add(nums[i])
    return result