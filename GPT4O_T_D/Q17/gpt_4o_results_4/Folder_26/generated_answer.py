def all_ints_div_by_both_two_nums(int_list):
    result = []
    if len(int_list) > 70:
        for num in int_list[69:71]:
            if num % 72 == 0 and num % 70 == 0:
                result.append(num)
    return result