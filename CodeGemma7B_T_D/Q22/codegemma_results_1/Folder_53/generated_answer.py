def find_sum_of_multiples(n):
    """
            Finds the sum of the first 60 possitive multiples of the given integer.
            """
    sum_of_multiples = 0
    for i in range(1, 61):
        sum_of_multiples += i * n
    return sum_of_multiples