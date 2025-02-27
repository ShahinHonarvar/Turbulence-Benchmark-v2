def sum_odd_ints_inclusive(numbers):
    odd_numbers = [num for num in numbers[43:52] if num % 2 != 0]
    return sum(odd_numbers)