def composite_nums_between_indices(nums):
    if len(nums) < 6:
        return set()
    composites = set()
    for num in nums[5:6]:
        if all((num % i != 0 for i in range(2, num))):
            continue
        composites.add(num)
    return composites