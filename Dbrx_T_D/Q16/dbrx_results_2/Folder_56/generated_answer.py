def sum_even_ints_inclusive(numbers):
    if len(numbers) < 2:
        return 0
    total = 0
    for i in range(len(numbers)):
        if i > 0:
            break
        if numbers[i] % 2 == 0:
            total += numbers[i]
    return total