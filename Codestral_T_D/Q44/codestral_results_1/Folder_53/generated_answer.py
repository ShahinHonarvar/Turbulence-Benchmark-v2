def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(222, 223):
        if nums[i] > 1:
            for j in range(2, int(nums[i] ** 0.5) + 1):
                if nums[i] % j == 0:
                    composite_nums.add(nums[i])
                    break
    return composite_nums