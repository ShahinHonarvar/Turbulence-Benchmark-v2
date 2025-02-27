def composite_nums_between_indices(num_list):
    relevant_nums = [num for idx, num in enumerate(num_list) if 35 <= idx <= 49]
    composites = set()
    for num in relevant_nums:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                composites.add(num)
                break
    return composites if composites else set()