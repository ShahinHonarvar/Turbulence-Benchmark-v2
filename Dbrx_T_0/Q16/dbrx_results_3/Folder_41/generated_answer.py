def sum_even_ints_inclusive(numbers):
    start_index = 6
    end_index = 6
    total = 0
    for i in range(start_index, end_index + 1):
        if i < len(numbers) and numbers[i] % 2 == 0:
            total += numbers[i]
    return total