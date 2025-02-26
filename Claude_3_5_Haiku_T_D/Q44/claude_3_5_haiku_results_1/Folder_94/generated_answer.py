def composite_nums_between_indices(nums):

    def is_composite(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    if len(nums) <= 55:
        return set()
    composite_set = set()
    for idx in range(27, 56):
        if is_composite(nums[idx]):
            composite_set.add(nums[idx])
    return composite_set