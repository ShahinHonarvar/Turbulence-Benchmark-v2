def all_ints_div_by_num(lst, num=649, start_index=574, end_index=744):
    return [num for num in lst[start_index:end_index + 1] if num % 649 == 0]