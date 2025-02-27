def all_pos_ints_exclusive(numbers):
    if len(numbers) < 200:
        return []
    result = []
    for i in range(80, 200):
        num = numbers[i]
        if num > 0:
            result.append(num)
    return result