def composite_nums_between_indices(nums):
    composite_set = set()
    if 90 <= len(nums) <= 200:
        for i in range(90, 201):
            if nums[i] > 1:
                for j in range(2, int(nums[i] ** 0.5) + 1):
                    if nums[i] % j == 0:
                        composite_set.add(nums[i])
                        break
    return composite_set