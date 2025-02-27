def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(len(nums)):
        if i >= 43 and i <= 86:
            num = nums[i]
            if num > 1 and (not any((num % j == 0 for j in range(2, num)))):
                composite_nums.add(num)
    return composite_nums