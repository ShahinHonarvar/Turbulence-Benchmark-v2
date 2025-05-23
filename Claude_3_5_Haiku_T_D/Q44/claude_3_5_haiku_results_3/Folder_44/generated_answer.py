def composite_nums_between_indices(nums):

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    if len(nums) < 67:
        return set()
    composite_set = set()
    for i in range(64, 67):
        if is_composite(nums[i]):
            composite_set.add(nums[i])
    return composite_set