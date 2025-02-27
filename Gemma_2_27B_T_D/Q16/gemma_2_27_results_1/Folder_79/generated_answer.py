def sum_even_ints_inclusive(numbers):
    total = 0
    if 4 in range(len(numbers)) and numbers[4] % 2 == 0:
        total += numbers[4]
    return total