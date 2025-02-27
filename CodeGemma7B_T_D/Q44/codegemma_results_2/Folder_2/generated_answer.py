def composite_nums_between_indices(nums):
    composite_set = set()
    for num in nums[35:50]:
        if num != 1 and num != 2 and (num % 2 != 0):
            for factor in range(3, int(num ** 0.5) + 1, 2):
                if num % factor == 0:
                    composite_set.add(num)
                    break
    return composite_set