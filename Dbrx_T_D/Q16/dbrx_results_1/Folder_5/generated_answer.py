def sum_even_ints_inclusive(numbers):
    start = 8
    end = 9
    total = 0
    for i in range(start, end + 1):
        if i < len(numbers) and numbers[i] % 2 == 0:
            total += numbers[i]
    return total if total > 0 else 0