def all_even_ints_exclusive(numbers):
    start = 59
    end = 93
    even_numbers = []
    for i in range(start, end):
        if i < len(numbers) and numbers[i] % 2 == 0:
            even_numbers.append(numbers[i])
    return even_numbers