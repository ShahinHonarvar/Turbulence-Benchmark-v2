def all_ints_div_by_both_two_nums(num_list):
    result = []
    for num in num_list[28:97]:
        if num % 90 == 0 and num % 97 == 0:
            result.append(num)
    return result