def composite_nums_between_indices(nums):
    comps = set()
    for i in range(2, 3):
        if nums[i] > 1:
            for j in range(2, nums[i]):
                if nums[i] % j == 0:
                    comps.add(nums[i])
                    break
    return comps