def composite_nums_between_indices(nums):
    res = set()
    for i in range(max(3, len(nums))):
        if 3 <= i <= 5 and nums[i] > 1:
            is_composite = False
            for j in range(2, int(nums[i] ** 0.5) + 1):
                if nums[i] % j == 0:
                    is_composite = True
                    break
            if is_composite:
                res.add(nums[i])
    return res