def sum_ints_div_by_either_nums(integer_list):
    total = 0
    for number in integer_list[93:95]:
        if number % -53 == 0 or number % -91 == 0:
            total += number
    return total if total else 0