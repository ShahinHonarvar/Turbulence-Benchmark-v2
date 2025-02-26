def all_ints_div_by_both_two_nums(integer_list):
    result = []
    for num in integer_list[13:19]:
        if num % 45 == 0 and num % 20 == 0:
            result.append(num)
    return result