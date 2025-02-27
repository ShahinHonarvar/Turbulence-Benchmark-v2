def composite_nums_between_indices(nums):
    result = set()
    for i in range(5, 8):
        if i < len(nums) and nums[i] > 1:
            for j in range(2, int(nums[i] ** 0.5) + 1):
                if nums[i] % j == 0:
                    result.add(nums[i])
                    break
    return result