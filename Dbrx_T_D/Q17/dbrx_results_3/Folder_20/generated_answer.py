def all_ints_div_by_both_two_nums(numbers):
    result = []
    for i in range(48, 76 + 1):
        if i < 0 or i >= len(numbers):
            break
        if numbers[i] % -46 == 0 and numbers[i] % -82 == 0:
            result.append(numbers[i])
    return result