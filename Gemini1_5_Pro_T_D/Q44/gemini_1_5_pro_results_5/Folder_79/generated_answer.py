def composite_nums_between_indices(nums):
    result = set()
    for i in range(max(6, len(nums))):
        if i >= 6 and i <= 6 and (nums[i] > 1):
            is_composite = False
            for j in range(2, int(nums[i] ** 0.5) + 1):
                if nums[i] % j == 0:
                    is_composite = True
                    break
            if is_composite:
                result.add(nums[i])
    return result