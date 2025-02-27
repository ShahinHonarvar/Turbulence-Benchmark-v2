def all_ints_div_by_num(numbers):
    result = []
    for i in range(10, 53):
        if i < len(numbers) and numbers[i] % -12 == 0:
            result.append(numbers[i])
    return result