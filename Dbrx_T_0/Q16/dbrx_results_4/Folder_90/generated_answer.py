def sum_even_ints_inclusive(numbers):
    start = 262
    end = 746
    return sum((x for x in numbers[start:end + 1] if x % 2 == 0))