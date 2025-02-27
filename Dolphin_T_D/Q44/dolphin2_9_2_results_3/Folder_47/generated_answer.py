def composite_nums_between_indices(nums):
    comp_nums = set()
    for i in range(75, 89):
        if nums[i] > 1:
            for j in range(2, nums[i]):
                if nums[i] % j == 0:
                    comp_nums.add(nums[i])
                    break
    return comp_nums