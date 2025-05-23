def composite_nums_between_indices(nums):

    def is_composite(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    composite_set = set()
    for i in range(5, min(8, len(nums))):
        if is_composite(nums[i]):
            composite_set.add(nums[i])
    return composite_set