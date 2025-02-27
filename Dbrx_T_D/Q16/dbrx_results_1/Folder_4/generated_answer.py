def sum_even_ints_inclusive(numbers):
    start_index = 12
    end_index = 92
    total = 0
    if end_index >= len(numbers):
        end_index = len(numbers) - 1
    for i in range(start_index, end_index + 1):
        if numbers[i] % 2 == 0:
            total += numbers[i]
    return total