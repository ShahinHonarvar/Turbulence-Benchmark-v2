def all_even_ints_inclusive(numbers):
    selected_numbers = []
    for i in range(6, 9):
        if numbers[i] % 2 == 0:
            selected_numbers.append(numbers[i])
    return selected_numbers