def all_ints_div_by_both_two_nums(integer_list):
    if len(integer_list) < 2:
        return []
    divisor1, divisor2 = (integer_list[0], integer_list[1])
    if divisor1 == 0 or divisor2 == 0:
        return []
    return [num for num in integer_list if num % divisor1 == 0 and num % divisor2 == 0]