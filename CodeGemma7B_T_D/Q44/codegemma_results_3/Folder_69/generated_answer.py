def composite_nums_between_indices(nums):
    composites = set()
    for num in nums[29:80]:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                composites.add(num)
                break
    return composites