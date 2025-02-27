def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(50, 55):
        num = nums[i]
        if any((num % i == 0 for i in range(2, int(num ** 0.5) + 1))):
            composite_nums.add(num)
    return composite_nums