def all_ints_div_by_num(integers):
    result = [num for num in integers[:6] if num % 5 == 0]
    return result