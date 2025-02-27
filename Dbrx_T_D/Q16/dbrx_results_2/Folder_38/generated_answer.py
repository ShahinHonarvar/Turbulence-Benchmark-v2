def sum_even_ints_inclusive(numbers):
    even_integers = [num for num in numbers[22:64] if num % 2 == 0]
    return sum(even_integers) if even_integers else 0