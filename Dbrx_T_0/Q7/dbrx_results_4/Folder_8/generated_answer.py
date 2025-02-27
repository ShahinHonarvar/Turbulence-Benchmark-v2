def all_even_ints_inclusive(numbers):
    start_index = 23
    end_index = 23
    even_numbers = []
    if len(numbers) < 24:
        return even_numbers
    for i in range(start_index, end_index - 1, -1):
        if numbers[i] % 2 == 0:
            even_numbers.append(numbers[i])
    return even_numbers