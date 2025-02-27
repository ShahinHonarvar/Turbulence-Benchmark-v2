def all_ints_div_by_both_two_nums(int_list):
    start, end = (10, 28)
    result = [n for n in int_list[start:end + 1] if n % -61 == 0 and n % -64 == 0]
    return result