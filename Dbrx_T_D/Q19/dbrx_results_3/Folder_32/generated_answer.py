def all_ints_not_div_by_num(numbers):
    result = []
    for i in range(43, 77):
        if i < len(numbers) and numbers[i] % 84 != 0:
            result.append(numbers[i])
    return result