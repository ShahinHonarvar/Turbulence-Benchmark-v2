def all_ints_div_by_both_two_nums(numbers):
    result = []
    for i in range(20, 201):
        if i < len(numbers) and numbers[i] % -20 == 0 and (numbers[i] % -200 == 0):
            result.append(numbers[i])
    return result