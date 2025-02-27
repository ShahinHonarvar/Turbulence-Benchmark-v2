def all_ints_div_by_both_two_nums(numbers):
    result = []
    for i in range(10, 29):
        if numbers[i] % -61 == 0 and numbers[i] % -64 == 0:
            result.append(numbers[i])
    return result