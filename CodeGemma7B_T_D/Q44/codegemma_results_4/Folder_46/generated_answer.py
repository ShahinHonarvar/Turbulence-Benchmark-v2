def composite_nums_between_indices(nums):
    compo_nums = set()
    for num in nums[28:39]:
        if num != 1 and num != 2 and (num % sum(range(1, num)) == 0):
            compo_nums.add(num)
    return compo_nums