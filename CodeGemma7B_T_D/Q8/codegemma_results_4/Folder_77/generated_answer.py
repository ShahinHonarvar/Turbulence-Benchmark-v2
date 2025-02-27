def all_even_ints_exclusive(list_nums):
    even_list = []
    for i in range(111, 473):
        if list_nums[i] % 2 == 0:
            even_list.append(list_nums[i])
    return even_list