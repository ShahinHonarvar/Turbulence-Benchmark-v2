def sum_even_ints_inclusive(numbers):
    return sum((x for x in numbers[8:81] if x % 2 == 0))