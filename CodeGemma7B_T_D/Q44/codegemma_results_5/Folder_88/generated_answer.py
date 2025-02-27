def composite_nums_between_indices(nums):
    composite_nums = []
    for i in range(8, 10):
        num = nums[i]
        if num > 1 and all((num % j != 0 for j in range(2, int(num ** 0.5) + 1))):
            composite_nums.append(num)
    return set(composite_nums)