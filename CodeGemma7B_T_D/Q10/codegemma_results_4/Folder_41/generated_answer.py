def all_odd_ints_exclusive(numbers):
    result = []
    for i in range(8, 10):
        if numbers[i] % 2 != 0:
            result.append(numbers[i])
    if not result:
        return []
    return result