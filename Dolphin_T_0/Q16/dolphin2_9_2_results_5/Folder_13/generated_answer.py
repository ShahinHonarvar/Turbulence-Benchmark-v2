def sum_even_ints_inclusive(numbers):
    """This function takes a list of integers as input and returns the sum
    of all even integers from index 25 to 87 inclusive. If no even integers exist
    in this range, returns 0"""
    return sum((num for num in numbers[25:88:2] if num % 2 == 0))