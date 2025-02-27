def all_ints_div_by_both_two_nums(numbers):
    result = []
    for i in range(14, 94):
        if numbers[i] % 71 == 0 and numbers[i] % 81 == 0:
            result.append(numbers[i])
    return result