def all_odd_ints_inclusive(numbers):
    if not isinstance(numbers, list):
        raise TypeError('Argument must be a list')
    result = []
    for i in range(1, 9):
        if i >= len(numbers):
            break
        if numbers[i] % 2 != 0:
            result.append(numbers[i])
    return result