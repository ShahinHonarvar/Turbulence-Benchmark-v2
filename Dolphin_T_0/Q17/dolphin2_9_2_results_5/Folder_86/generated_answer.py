def all_ints_div_by_both_two_nums(int_list):
    result = []
    for num in int_list[54:80]:
        if num % 54 == 0 and num % 28 == 0:
            result.append(num)
    return result