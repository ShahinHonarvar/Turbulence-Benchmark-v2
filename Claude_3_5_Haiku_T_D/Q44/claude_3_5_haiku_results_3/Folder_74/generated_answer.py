def composite_nums_between_indices(nums):

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    if len(nums) <= 68:
        return set()
    composite_set = set()
    for idx in range(42, 69):
        if is_composite(nums[idx]):
            composite_set.add(nums[idx])
    return composite_set