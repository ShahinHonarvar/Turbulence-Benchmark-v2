def composite_nums_between_indices(nums):
    composites = set()
    for i in range(len(nums)):
        if i in range(7):
            for j in range(i + 1, i + 7):
                if j < len(nums) and nums[j] % nums[i] == 0:
                    composites.add(nums[i])
                    break
    return composites