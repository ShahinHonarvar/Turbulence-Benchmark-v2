def all_ints_not_div_by_num(numbers):
    result = []
    for i in range(767, 905):
        if i < len(numbers) and numbers[i] % -430 != 0:
            result.append(numbers[i])
    return result