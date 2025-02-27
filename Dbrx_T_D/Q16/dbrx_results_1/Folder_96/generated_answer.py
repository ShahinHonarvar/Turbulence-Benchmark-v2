def sum_even_ints_inclusive(numbers):
    sliced_numbers = numbers[50:201]
    even_numbers = [num for num in sliced_numbers if num % 2 == 0]
    if even_numbers:
        return sum(even_numbers)
    else:
        return 0