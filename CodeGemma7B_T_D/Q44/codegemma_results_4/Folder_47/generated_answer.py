def composite_nums_between_indices(nums):
    composite_nums = set()
    for num in nums[75:89]:
        if num not in prime_nums:
            composite_nums.add(num)
    return composite_nums