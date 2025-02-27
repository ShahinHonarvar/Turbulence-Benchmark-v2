def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(19, 93):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    composite_nums.add(nums[i])
                    break
    return composite_nums