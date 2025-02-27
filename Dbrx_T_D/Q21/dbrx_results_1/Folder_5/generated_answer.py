def all_ints_div_by_num(numbers):
    result = []
    for i in range(1, 5):
        if i < len(numbers) and numbers[i] % -6 == 0:
            result.append(numbers[i])
    return result