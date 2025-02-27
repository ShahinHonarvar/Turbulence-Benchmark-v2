def composite_nums_between_indices(lst):
    composite_nums = set()
    for i in range(29, 80):
        if not is_prime(lst[i]):
            composite_nums.add(lst[i])
    return composite_nums