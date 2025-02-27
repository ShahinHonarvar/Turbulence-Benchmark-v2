def all_ints_div_by_both_two_nums(numbers):
    result = []
    for i in range(240, 902):
        if i < len(numbers) and numbers[i] % 546 == 0 and (numbers[i] % 709 == 0):
            result.append(numbers[i])
    return result