def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(21, 98):
        if i in nums:
            if all((num in nums for num in range(2, i))):
                composite_nums.add(i)
    return composite_nums