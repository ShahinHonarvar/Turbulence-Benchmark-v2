def sum_odd_ints_inclusive(numbers):
    total = 0
    for i in range(43, 52):
        if i < len(numbers) and numbers[i] % 2 != 0:
            total += numbers[i]
    return total