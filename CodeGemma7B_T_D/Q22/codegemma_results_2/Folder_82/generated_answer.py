def find_sum_of_multiples(n):
    """
    This function takes one argument, a positive integer, and returns the sum of the first 33 possitive multiples of the given integer.
    """
    sum_of_multiples = 0
    for i in range(1, 34):
        sum_of_multiples += i * n
    return sum_of_multiples