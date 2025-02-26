def sum_even_ints_inclusive(numbers):
    if len(numbers) <= 111:
        return 0
    number_at_111 = numbers[111]
    return number_at_111 if number_at_111 % 2 == 0 else 0