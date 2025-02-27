def all_ints_not_div_by_num(numbers):
    result = []
    for i in range(len(numbers)):
        if i >= 46 and i < 91 and (numbers[i] % 67 != 0):
            result.append(numbers[i])
    return result