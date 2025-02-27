def all_ints_div_by_both_two_nums(numbers):
    result = []
    for i in range(20, min(200, len(numbers))):
        if numbers[i] % -20 == 0 and numbers[i] % -200 == 0:
            result.append(numbers[i])
    return result