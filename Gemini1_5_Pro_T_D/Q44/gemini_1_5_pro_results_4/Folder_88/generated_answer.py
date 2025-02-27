def composite_nums_between_indices(nums):
    res = set()
    for i in range(max(8, len(nums))):
        if i >= 8 and i <= 9 and (nums[i] > 1):
            for j in range(2, int(nums[i] ** 0.5) + 1):
                if nums[i] % j == 0:
                    res.add(nums[i])
                    break
    return res