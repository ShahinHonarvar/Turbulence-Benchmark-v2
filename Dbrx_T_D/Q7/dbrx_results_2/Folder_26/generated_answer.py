def all_even_ints_inclusive(numbers):
    even_numbers = []
    for i in range(min(62, len(numbers)), min(100, len(numbers))):
        if numbers[i] % 2 == 0:
            even_numbers.append(numbers[i])
    return even_numbers