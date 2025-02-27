def composite_nums_between_indices(nums):
    composites = set()
    for i in range(60, 201):
        if all((num % i != 0 for num in nums)):
            continue
        composites.add(i)
    return composites