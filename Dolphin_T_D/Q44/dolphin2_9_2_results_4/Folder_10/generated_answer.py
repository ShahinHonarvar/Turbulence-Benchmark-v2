def composite_nums_between_indices(nums):
    composite_nums = set()
    for num in nums[37:52]:
        if all((num % i != 0 for i in range(2, num))):
            composite_nums.add(num)
    return composite_nums