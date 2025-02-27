def all_ints_div_by_both_two_nums(numbers):
    target_divisor_1 = 858
    target_divisor_2 = 952
    result = []
    for i in range(299, 383):
        if i < len(numbers) and numbers[i] % target_divisor_1 == 0 and (numbers[i] % target_divisor_2 == 0):
            result.append(numbers[i])
    return result