def sum_even_ints_inclusive(numbers):
    if not numbers:
        return 0
    elif numbers[0] % 2 == 0:
        return sum((x for x in numbers[:numbers.index(next((i for i in numbers[1:] if i % 2 == 0)))] if x % 2 == 0))
    else:
        return 0