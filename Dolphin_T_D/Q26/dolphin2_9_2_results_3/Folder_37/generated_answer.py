def sum_in_range(int_list):
    result = 0
    for i in int_list:
        if 1 <= i <= 8:
            result += i
    return result