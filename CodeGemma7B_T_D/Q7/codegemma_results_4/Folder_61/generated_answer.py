def all_even_ints_inclusive(lst):
    even_nums = []
    for i in range(7, 7 + 1):
        if lst[i] % 2 == 0:
            even_nums.append(lst[i])
    return even_nums