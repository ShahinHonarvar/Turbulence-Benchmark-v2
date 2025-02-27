def composite_nums_between_indices(nums):
    composite_nums = set()
    for num in nums[0:8]:
        if num > 1 and all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            composite_nums.add(num)
    return composite_nums