def all_pos_ints_inclusive(numbers):
    if len(numbers) < 95:
        return []
    pos_ints = []
    for i in range(75, 95):
        num = numbers[i]
        if num > 0:
            pos_ints.append(num)
    return pos_ints