def composite_nums_between_indices(nums):
    composite_set = set()
    for i in range(1, 2):
        for j in range(len(nums)):
            if j >= i and nums[j] > 1 and (not (j == i and nums[j] == 2)):
                is_composite = False
                for k in range(2, int(nums[j] ** 0.5) + 1):
                    if nums[j] % k == 0:
                        is_composite = True
                        break
                if is_composite:
                    composite_set.add(nums[j])
    return composite_set