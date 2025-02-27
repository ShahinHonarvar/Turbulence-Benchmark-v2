def sum_even_ints_inclusive(numbers):
    start = 5
    end = 7
    even_ints = [num for num in numbers[start:end + 1] if num % 2 == 0]
    return sum(even_ints) if even_ints else 0