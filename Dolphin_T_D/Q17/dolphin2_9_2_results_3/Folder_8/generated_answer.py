def all_ints_div_by_both_two_nums(numbers):
    result = []
    for i in range(36, 86):
        if numbers[i] % -27 == 0 and numbers[i] % -96 == 0:
            result.append(numbers[i])
    return result