def all_ints_not_div_by_num(list):
    filtered_list = [number for number in list[38:52] if number % -41 != 0]
    if not filtered_list:
        return []
    else:
        return filtered_list