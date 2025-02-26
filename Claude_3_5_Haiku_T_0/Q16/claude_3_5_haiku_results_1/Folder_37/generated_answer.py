def sum_even_ints_inclusive(numbers):
    return sum((num for num in numbers[1:6] if num % 2 == 0))