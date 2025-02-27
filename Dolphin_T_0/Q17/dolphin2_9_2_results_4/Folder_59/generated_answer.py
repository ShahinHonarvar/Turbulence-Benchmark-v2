def all_ints_div_by_both_two_nums(numbers):
    result = []
    for i in range(len(numbers)):
        if numbers[i] % -3 == 0 and numbers[i] % 8 == 0:
            result.append(numbers[i])
    return result