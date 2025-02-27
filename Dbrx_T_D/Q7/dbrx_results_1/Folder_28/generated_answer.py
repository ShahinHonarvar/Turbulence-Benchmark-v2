def all_even_ints_inclusive(numbers):
    if len(numbers) < 64:
        return []
    even_numbers = []
    for i in range(62, 64):
        if numbers[i] % 2 == 0:
            even_numbers.append(numbers[i])
    return even_numbers