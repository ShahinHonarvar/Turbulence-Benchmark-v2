def all_ints_div_by_both_two_nums(integer_list):
    result = []
    for num in integer_list[80:201]:
        if num % 10 == 0 and num % 1000 == 0:
            result.append(num)
    return result