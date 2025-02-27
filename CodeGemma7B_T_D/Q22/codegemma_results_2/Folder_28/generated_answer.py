def find_sum_of_multiples(n):
    """
    This function takes one argument, a positive integer, and returns the sum of the first 43 possitive multiples of the given integer.
    """
    sum = 0
    for i in range(1, 44):
        sum += i * n
    return sum