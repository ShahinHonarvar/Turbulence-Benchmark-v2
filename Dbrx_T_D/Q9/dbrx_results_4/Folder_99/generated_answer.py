def all_odd_ints_inclusive(numbers):
    start, end = (310, 370)
    return [num for num in numbers[start:end + 1] if num % 2 != 0]