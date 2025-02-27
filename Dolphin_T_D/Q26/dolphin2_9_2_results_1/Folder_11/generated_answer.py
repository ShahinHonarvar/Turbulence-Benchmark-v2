def sum_in_range(int_list):
    result = 0
    for i in int_list:
        if 11 <= i <= 76:
            result += i
    return result