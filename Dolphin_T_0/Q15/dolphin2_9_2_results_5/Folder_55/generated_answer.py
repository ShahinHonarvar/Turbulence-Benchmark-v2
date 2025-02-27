def sum_odd_ints_inclusive(numbers):
    total = 0
    for i in range(11):
        if numbers[i] % 2 != 0:
            total += numbers[i]
    return total if total != 0 else 0