def all_even_ints_exclusive(numbers):
    start_index = 275
    end_index = 376
    even_numbers = []
    for i in range(start_index, end_index):
        if i < len(numbers) and numbers[i] % 2 == 0:
            even_numbers.append(numbers[i])
    return even_numbers