def composite_nums_between_indices(nums):
    composite_nums = set()
    for num in nums[62:64]:
        if num > 1 and (not all((num % d for d in range(2, int(num ** 0.5) + 1)))):
            composite_nums.add(num)
    return composite_nums