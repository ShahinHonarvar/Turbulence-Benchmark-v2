def all_pos_ints_exclusive(numbers):
    if len(numbers) < 98:
        return []
    result = []
    for i in range(70, 98):
        num = numbers[i]
        if num > 0:
            result.append(num)
    return result