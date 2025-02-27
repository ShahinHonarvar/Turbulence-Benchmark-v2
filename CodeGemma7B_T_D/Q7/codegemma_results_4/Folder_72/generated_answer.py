def all_even_ints_inclusive(lst):
    if len(lst) <= 29 or len(lst) < 51:
        return []
    lower_limit = 29
    upper_limit = 51
    even_nums = []
    for index in range(len(lst)):
        if lst[index] == lower_limit:
            for num in range(index, len(lst)):
                if lst[num] <= upper_limit and lst[num] % 2 == 0:
                    even_nums.append(lst[num])
    return even_nums