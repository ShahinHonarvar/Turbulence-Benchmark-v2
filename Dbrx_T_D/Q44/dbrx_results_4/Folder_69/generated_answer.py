def composite_nums_between_indices(nums):
    set_of_composite_nums = set()
    for i in range(len(nums)):
        if i >= 29 and i <= 79:
            if nums[i] > 1:
                for j in range(2, nums[i]):
                    if nums[i] % j == 0:
                        set_of_composite_nums.add(nums[i])
                        break
    return set_of_composite_nums