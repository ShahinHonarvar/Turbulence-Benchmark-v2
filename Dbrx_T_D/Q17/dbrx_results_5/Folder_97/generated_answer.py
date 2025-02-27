def all_ints_div_by_both_two_nums(numbers):
    result = []
    for i in range(58, 76):
        if i < len(numbers) and numbers[i] % 72 == 0 and (numbers[i] % 62 == 0):
            result.append(numbers[i])
    return result