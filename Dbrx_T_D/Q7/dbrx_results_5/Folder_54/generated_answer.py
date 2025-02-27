def all_even_ints_inclusive(numbers):
    even_numbers = []
    for i in range(34, 56):
        if i < len(numbers) and numbers[i] % 2 == 0:
            even_numbers.append(numbers[i])
    return even_numbers