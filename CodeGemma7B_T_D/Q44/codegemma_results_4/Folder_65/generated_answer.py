def composite_nums_between_indices(nums):
    composites = set()
    for num in nums[82:87]:
        for i in range(2, num):
            if num % i == 0:
                composites.add(num)
                break
    return composites