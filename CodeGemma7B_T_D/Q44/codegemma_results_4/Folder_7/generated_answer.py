def composite_nums_between_indices(nums):
    composites = set()
    for num in nums[527:539]:
        for i in range(2, int(num ** (1 / 2)) + 1):
            if num % i == 0:
                composites.add(num)
                break
    return composites