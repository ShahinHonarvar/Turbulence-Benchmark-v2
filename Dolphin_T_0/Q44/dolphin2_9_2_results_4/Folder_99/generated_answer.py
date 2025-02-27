def composite_nums_between_indices(nums):
    composite_nums = set()
    for num in nums[246:751]:
        if any((num % i == 0 for i in range(2, num))):
            composite_nums.add(num)
    return composite_nums