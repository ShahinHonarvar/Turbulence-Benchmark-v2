def all_pos_ints_inclusive(numbers):
    result = []
    for i in range(22, 51):
        if i in numbers:
            result.append(i)
    return result if result else []