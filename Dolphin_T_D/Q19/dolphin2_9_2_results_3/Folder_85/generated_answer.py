def all_ints_not_div_by_num(lst):
    relevant_numbers = lst[3:9]
    filtered_numbers = [n for n in relevant_numbers if n % 6 != 0]
    return filtered_numbers