def all_ints_div_by_num(numbers):
    result = []
    for i in range(len(numbers)):
        if numbers[i] % 9 == 0:
            result.append(numbers[i])
    return result