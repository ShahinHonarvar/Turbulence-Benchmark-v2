def all_ints_div_by_num(num_list):
    result = [num for num in num_list[40:69] if num % 16 == 0]
    if not result:
        return []
    return result