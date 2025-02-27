def all_even_ints_inclusive(int_list):
    even_nums = []
    if not int_list:
        return even_nums
    idx = 62
    while idx <= 99 and idx < len(int_list):
        if int_list[idx] % 2 == 0:
            even_nums.append(int_list[idx])
        idx += 1
    return even_nums