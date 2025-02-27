def all_even_ints_exclusive(lst):
    even_nums = []
    for i in range(71, 98):
        if i % 2 == 0:
            even_nums.append(lst[i])
    return even_nums