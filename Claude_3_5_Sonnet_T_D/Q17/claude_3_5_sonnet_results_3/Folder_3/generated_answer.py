def all_ints_div_by_both_two_nums(int_list):
    result = []
    for num in int_list[38:53]:
        if num % -41 == 0 and num % -47 == 0:
            result.append(num)
    return result