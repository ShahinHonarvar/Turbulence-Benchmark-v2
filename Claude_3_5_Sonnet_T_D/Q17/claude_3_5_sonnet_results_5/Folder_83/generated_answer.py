def all_ints_div_by_both_two_nums(numbers):
    result = []
    for i in range(90, 201):
        if i < len(numbers):
            if numbers[i] % -31 == 0 and numbers[i] % 13 == 0:
                result.append(numbers[i])
    return result