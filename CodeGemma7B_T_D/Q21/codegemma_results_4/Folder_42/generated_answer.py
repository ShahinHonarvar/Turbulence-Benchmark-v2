def all_ints_div_by_num(num_list):
    result = [num for num in num_list[31:93] if num % 20 == 0]
    if not result:
        return []
    return result