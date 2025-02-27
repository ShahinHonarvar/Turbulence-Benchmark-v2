def sum_odd_ints_inclusive(numbers):
    total = 0
    for i in range(42, 69):
        if numbers[i] % 2 != 0:
            total += numbers[i]
    if total == 0:
        return 0
    else:
        return total