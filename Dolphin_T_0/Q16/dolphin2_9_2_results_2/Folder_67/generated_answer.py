def sum_even_ints_inclusive(ints):
    if not ints:
        return 0
    even_numbers = [i for i in ints[22:51] if i % 2 == 0]
    return sum(even_numbers) if even_numbers else 0