def composite_nums_between_indices(nums):
    for i in range(4, len(nums) + 1):
        if i in nums:
            if i % 2 == 0:
                continue
            for j in range(2, i):
                if i % j == 0:
                    composite_set = set()
                    composite_set.add(i)
                    return composite_set
    return set()