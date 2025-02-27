def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(max(32, len(nums) - (35 - len(nums))), min(35, len(nums))):
        if nums[i] > 1 and (not nums[i] & 1) and (nums[i] % 3 != 0):
            composite_nums.add(nums[i])
        for j in range(5, int(nums[i] ** 0.5) + 1, 2):
            if nums[i] % j == 0:
                composite_nums.add(nums[i])
                break
    return composite_nums