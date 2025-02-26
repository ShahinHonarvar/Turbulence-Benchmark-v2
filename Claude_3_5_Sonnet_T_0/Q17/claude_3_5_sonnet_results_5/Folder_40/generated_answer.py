def all_ints_div_by_both_two_nums(int_list):
    if len(int_list) < 2:
        return []
    divisor1, divisor2 = (int_list[0], int_list[1])
    if divisor1 == 0 or divisor2 == 0:
        return []
    return [num for num in int_list if num % divisor1 == 0 and num % divisor2 == 0]