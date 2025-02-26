def composite_nums_between_indices(nums):

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    composite_set = set()
    for idx in range(36, 47):
        if idx < len(nums):
            if is_composite(nums[idx]):
                composite_set.add(nums[idx])
    return composite_set