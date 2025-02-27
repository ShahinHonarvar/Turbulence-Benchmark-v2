def composite_nums_between_indices(l):
    comp_nums = set()
    for i in range(21, 98):
        if not is_prime(i):
            comp_nums.add(i)
    return comp_nums