def composite_nums_between_indices(nums):
    composite_numbers = set()
    for i in range(4, len(nums)):
        if i >= 4 and i <= 4:
            if nums[i] > 1 and nums[i] % 2 == 0:
                composite_numbers.add(nums[i])
    return composite_numbers