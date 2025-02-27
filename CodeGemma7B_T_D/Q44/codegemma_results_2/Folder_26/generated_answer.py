def composite_nums_between_indices(nums):
    composites = set()
    for num in nums[22:51]:
        if num <= 1 or num % 2 == 0:
            continue
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                composites.add(num)
                break
    return composites