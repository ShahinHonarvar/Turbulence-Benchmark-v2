def all_ints_div_by_num(num_list):
    result = [num for num in num_list[12:78] if num % -19 == 0]
    if not result:
        return []
    return result