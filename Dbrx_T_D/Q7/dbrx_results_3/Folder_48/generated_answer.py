def all_even_ints_inclusive(numbers):
    start, end = (533, 605)
    return [num for num in numbers[start:end + 1] if num % 2 == 0]