def composite_nums_between_indices(nums):
    if len(nums) < 201 or len(nums) < 20:
        return set()
    result = set()
    for i in range(20, 201):
        if nums[i] > 1 and (not all((nums[i] % j for j in range(2, int(nums[i] ** 0.5) + 1)))):
            result.add(nums[i])
    return result