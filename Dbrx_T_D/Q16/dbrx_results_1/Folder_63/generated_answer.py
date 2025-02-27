def sum_even_ints_inclusive(numbers):
    start, end = (22, 88)
    even_sum = sum((x for x in numbers[start:end + 1] if x % 2 == 0))
    return even_sum if even_sum != 0 else 0