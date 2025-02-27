def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(nums[0], nums[9] + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                composite_nums.add(i)
                break
    return composite_nums