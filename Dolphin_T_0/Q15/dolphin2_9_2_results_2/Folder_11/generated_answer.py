def sum_odd_ints_inclusive(input_list):
    result = 0
    if 37 <= 51 < len(input_list):
        for i in range(37, 52):
            if input_list[i] % 2 != 0:
                result += input_list[i]
    return result