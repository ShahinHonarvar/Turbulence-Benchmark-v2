def all_ints_div_by_num(lst):
    found = [num for i, num in enumerate(lst) if 26 <= i <= 74 and num % 80 == 0]
    return found