def sum_even_ints_inclusive(numbers):
    start = 262
    end = 746
    total = 0
    for i in range(start, end + 1):
        if i < len(numbers) and i >= 0 and (numbers[i] % 2 == 0):
            total += numbers[i]
    return total