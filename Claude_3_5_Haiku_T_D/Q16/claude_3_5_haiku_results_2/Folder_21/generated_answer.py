def sum_even_ints_inclusive(numbers):
    if len(numbers) <= 975:
        return 0
    subset = numbers[639:976]
    return sum((num for num in subset if num % 2 == 0))