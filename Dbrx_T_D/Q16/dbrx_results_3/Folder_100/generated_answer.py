def sum_even_ints_inclusive(numbers):
    start = 42
    end = 68
    total = 0
    if end >= len(numbers):
        end = len(numbers) - 1
    for i in range(start, end + 1):
        if i < 0 or i >= len(numbers):
            break
        if numbers[i] % 2 == 0:
            total += numbers[i]
    return total