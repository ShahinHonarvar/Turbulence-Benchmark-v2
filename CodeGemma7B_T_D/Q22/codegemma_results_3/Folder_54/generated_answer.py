def find_sum_of_multiples(number):
    """
            The function `find_sum_of_multiples` takes one argument, a positive integer, and returns the sum of the first 29 possitive multiples of the given integer.
            """
    sum_of_multiples = 0
    for i in range(1, 30):
        multiples = i * number
        sum_of_multiples += multiples
    return sum_of_multiples