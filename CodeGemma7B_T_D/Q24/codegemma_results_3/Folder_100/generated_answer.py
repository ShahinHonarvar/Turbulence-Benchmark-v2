def sum_of_divisors_in_range(n):
    """
            Write a function called 'sum_of_divisors_in_range' that takes a positive integer as its argument,
            and returns the sum of all positive divisors of the given integer that are between 11 and 41, both inclusive.
            If no such divisors exist in the specified range, the function should return 0.
            """
    if n <= 0:
        return 0
    sum_of_divisors = 0
    for i in range(11, 42):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors