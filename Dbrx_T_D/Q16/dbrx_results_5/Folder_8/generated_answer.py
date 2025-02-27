def sum_even_ints_inclusive(numbers):
    start_index = min(23, len(numbers) - 1)
    end_index = start_index
    sum = 0
    for i in range(start_index, max(0, start_index - 23), -1):
        if numbers[i] % 2 == 0:
            sum += numbers[i]
            if i - 1 >= 0:
                end_index = end_index - 1
    for i in range(end_index, max(0, start_index - 23), -1):
        if numbers[i] % 2 == 0:
            sum -= numbers[i]
    return sum if sum > 0 else 0