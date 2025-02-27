def sum_even_ints_inclusive(numbers):
    even_ints = [n for n in numbers[:11] if n % 2 == 0]
    return sum(even_ints) if even_ints else 0