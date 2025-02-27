def all_ints_div_by_num(numbers):
    result = []
    for i in range(31, 73):
        if numbers[i] % -63 == 0:
            result.append(numbers[i])
    return result