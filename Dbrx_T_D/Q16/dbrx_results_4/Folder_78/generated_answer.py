def sum_even_ints_inclusive(numbers):
    start_index = 43
    end_index = 51
    even_sum = 0
    for i in range(start_index, end_index + 1):
        if i < len(numbers) and numbers[i] % 2 == 0:
            even_sum += numbers[i]
    return even_sum