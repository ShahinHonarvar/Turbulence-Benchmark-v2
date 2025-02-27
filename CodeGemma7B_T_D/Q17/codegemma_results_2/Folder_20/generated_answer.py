def all_ints_div_by_both_two_nums(num_list):
    result = []
    for number in range(48, 77):
        if number % -46 == 0 and number % -82 == 0:
            result.append(number)
    return result