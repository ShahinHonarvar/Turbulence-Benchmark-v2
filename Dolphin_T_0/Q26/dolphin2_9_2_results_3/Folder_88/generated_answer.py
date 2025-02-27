def sum_in_range(numb_list):
    result = 0
    for numb in numb_list:
        if 1 <= numb <= 7:
            result += numb
    return result