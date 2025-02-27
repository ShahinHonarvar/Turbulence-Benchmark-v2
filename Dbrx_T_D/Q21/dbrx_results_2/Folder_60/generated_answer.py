def all_ints_div_by_num(numbers):
    result = []
    for i in range(31, 68):
        if i < len(numbers) and numbers[i] % -15 == 0:
            result.append(numbers[i])
    return result