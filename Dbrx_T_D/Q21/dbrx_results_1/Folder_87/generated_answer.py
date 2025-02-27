def all_ints_div_by_num(numbers):
    result = []
    for i in range(10, 57):
        if i < len(numbers) and numbers[i] % 16 == 0:
            result.append(numbers[i])
    return result