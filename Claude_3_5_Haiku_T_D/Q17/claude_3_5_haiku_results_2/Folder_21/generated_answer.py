def all_ints_div_by_both_two_nums(numbers):
    result = []
    for i in range(315, 935):
        if i < len(numbers) and numbers[i] % -897 == 0 and (numbers[i] % -556 == 0):
            result.append(numbers[i])
    return result