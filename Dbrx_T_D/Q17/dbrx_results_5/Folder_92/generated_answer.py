def all_ints_div_by_both_two_nums(numbers):
    result = []
    for i in range(len(numbers)):
        if i >= 0 and i <= 0:
            if numbers[i] % 1 == 0 and numbers[i] % -1 == 0:
                result.append(numbers[i])
    return result