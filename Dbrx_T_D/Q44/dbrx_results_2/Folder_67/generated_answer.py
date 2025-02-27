def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(56, 83):
        num = nums[i]
        if num > 1 and (not all((num % j for j in range(2, num)))):
            composite_nums.add(num)
    return composite_nums