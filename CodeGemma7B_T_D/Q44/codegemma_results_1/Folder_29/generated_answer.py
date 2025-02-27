def composite_nums_between_indices(nums):
    composite_numbers = set()
    for i in range(52, 72):
        if nums[i] % 2 == 0 or nums[i] % 3 == 0 or nums[i] % 5 == 0 or (nums[i] % 7 == 0):
            composite_numbers.add(nums[i])
    return composite_numbers