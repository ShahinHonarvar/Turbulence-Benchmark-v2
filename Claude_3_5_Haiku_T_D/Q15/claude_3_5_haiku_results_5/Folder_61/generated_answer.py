def sum_odd_ints_inclusive(numbers):
    total = 0
    for i in range(min(8, len(numbers))):
        if numbers[i] % 2 != 0:
            total += numbers[i]
    return total