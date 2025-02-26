def sum_odd_ints_inclusive(numbers):
    if len(numbers) <= 924:
        return 0
    total = 0
    for i in range(661, 925):
        if numbers[i] % 2 != 0:
            total += numbers[i]
    return total