def all_odd_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers[1:7], start=1) if num % 2 != 0]