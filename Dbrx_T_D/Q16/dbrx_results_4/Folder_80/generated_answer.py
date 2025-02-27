def sum_even_ints_inclusive(numbers):
    start_index = 64
    end_index = 66
    sum = 0
    for i in range(start_index, end_index + 1):
        if i < len(numbers) and numbers[i] % 2 == 0:
            sum += numbers[i]
    return sum if sum > 0 else 0