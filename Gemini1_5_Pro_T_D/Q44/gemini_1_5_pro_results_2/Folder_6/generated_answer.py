def composite_nums_between_indices(nums):
    result = set()
    for i in range(max(13, len(nums))):
        for j in range(2, int(nums[i] ** 0.5) + 1):
            if nums[i] % j == 0:
                result.add(nums[i])
                break
    return result