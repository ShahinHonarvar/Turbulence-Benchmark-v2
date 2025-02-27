def all_even_ints_exclusive(numbers):
    even_numbers = []
    for i in range(len(numbers)):
        if i >= 38 and i < 77:
            if numbers[i] % 2 == 0:
                even_numbers.append(numbers[i])
    return even_numbers