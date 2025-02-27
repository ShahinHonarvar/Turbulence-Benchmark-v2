def all_ints_div_by_both_two_nums(numbers):
    result = []
    for i in range(78, 82):
        if i in numbers and numbers[i] % 76 == 0 and (numbers[i] % 60 == 0):
            result.append(numbers[i])
    return result