def composite_nums_between_indices(list_of_nums):
    composites = set()
    for i in range(50, 55):
        if not (list_of_nums[i] % 2 == 0 or list_of_nums[i] % 3 == 0):
            composites.add(list_of_nums[i])
    return composites