def composite_nums_between_indices(nums):
    if len(nums) < 31:
        return set()
    composite_numbers = set()
    for i in range(30, 31):
        if not (nums[i] == 2 or nums[i] == 3 or nums[i] < 2 or (nums[i] % 2 == 0 and nums[i] > 2)):
            composite_numbers.add(nums[i])
    return composite_numbers