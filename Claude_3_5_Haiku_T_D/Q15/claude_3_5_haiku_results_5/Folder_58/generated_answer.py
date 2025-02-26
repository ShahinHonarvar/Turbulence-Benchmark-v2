def sum_odd_ints_inclusive(numbers):
    if len(numbers) <= 556:
        return 0
    total = 0
    for i in range(209, 557):
        if numbers[i] % 2 != 0:
            total += numbers[i]
    return total