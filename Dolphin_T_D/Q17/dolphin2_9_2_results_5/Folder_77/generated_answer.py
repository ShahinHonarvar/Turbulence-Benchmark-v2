def all_ints_div_by_both_two_nums(numbers):
    result = []
    for i in range(828, 933):
        if numbers[i] % -649 == 0 and numbers[i] % -461 == 0:
            result.append(numbers[i])
    return result