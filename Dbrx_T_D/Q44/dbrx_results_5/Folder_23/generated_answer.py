def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(len(nums)):
        if i >= 20 and i <= 30:
            if nums[i] > 1 and (not nums[i] == 2) and (nums[i] % 2 == 0):
                composite_nums.add(nums[i])
            elif nums[i] > 3:
                for j in range(3, int(nums[i] ** 0.5) + 1, 2):
                    if nums[i] % j == 0:
                        composite_nums.add(nums[i])
                        break
    return composite_nums