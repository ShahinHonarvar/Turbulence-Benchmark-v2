def composite_nums_between_indices(nums):
    composites = set()
    for num in nums[26:53]:
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                composites.add(num)
                break
    return composites