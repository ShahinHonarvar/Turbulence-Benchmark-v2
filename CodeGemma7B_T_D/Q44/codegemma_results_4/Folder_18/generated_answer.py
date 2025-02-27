def composite_nums_between_indices(nums):
    nums_between_indices = nums[25:88]
    composite_nums = set()
    for num in nums_between_indices:
        if num > 1 and num % 2 != 0 and any((num % div == 0 for div in range(3, int(num ** 0.5) + 1, 2))):
            composite_nums.add(num)
    return composite_nums if composite_nums else set()