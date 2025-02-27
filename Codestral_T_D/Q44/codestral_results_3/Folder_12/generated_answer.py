def composite_nums_between_indices(nums):
    composites = set()
    for i in range(51, 87):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    composites.add(nums[i])
                    break
    return composites