def all_ints_div_by_both_two_nums(numbers):
    result = []
    for i in range(20, 94):
        if numbers[i] % -92 == 0 and numbers[i] % -50 == 0:
            result.append(numbers[i])
    return result