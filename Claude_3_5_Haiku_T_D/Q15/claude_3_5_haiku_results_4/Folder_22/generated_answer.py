def sum_odd_ints_inclusive(numbers):
    if len(numbers) <= 41:
        return 0
    total = 0
    for index in range(40, 42):
        if numbers[index] % 2 != 0:
            total += numbers[index]
    return total