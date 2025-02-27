def sum_even_ints_inclusive(numbers):
    total = 0
    for i in range(22, 51):
        if numbers[i] % 2 == 0:
            total += numbers[i]
    return total if total else 0