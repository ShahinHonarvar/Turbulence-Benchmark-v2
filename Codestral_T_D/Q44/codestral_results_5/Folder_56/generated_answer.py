def composite_nums_between_indices(nums):

    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    result = set()
    if nums[0] > 1:
        for i in range(2, nums[0] + 1):
            if is_composite(i):
                result.add(i)
    return result