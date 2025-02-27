def all_even_ints_inclusive(num_list):
    even_nums = []
    for i in range(73, 74):
        if num_list[i] % 2 == 0:
            even_nums.append(num_list[i])
    return even_nums