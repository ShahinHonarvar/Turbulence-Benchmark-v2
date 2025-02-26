def all_ints_div_by_both_two_nums(integer_list):
    result = []
    for num in integer_list[55:67]:
        if num % 22 == 0 and num % 82 == 0:
            result.append(num)
    return result