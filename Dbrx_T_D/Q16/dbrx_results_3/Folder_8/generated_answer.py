def sum_even_ints_inclusive(numbers):
    start_index = 23
    end_index = 23
    sum = 0
    for i in range(start_index, end_index + 1):
        if i < 0 or i >= len(numbers):
            break
        if numbers[i] % 2 == 0:
            sum += numbers[i]
    return sum