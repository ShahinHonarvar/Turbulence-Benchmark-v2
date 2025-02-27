def composite_nums_between_indices(nums):
    com_nums = set()
    for num in nums[56:83]:
        if not num % 2 or num % 3 == 0:
            com_nums.add(num)
    return com_nums