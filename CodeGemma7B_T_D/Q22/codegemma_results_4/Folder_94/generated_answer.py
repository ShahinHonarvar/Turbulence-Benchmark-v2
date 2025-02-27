def find_sum_of_multiples(n):
    """
            Return the sum of the first 69 positive multiples of the given integer.
            """
    multiples = []
    for i in range(1, 70):
        multiples.append(i * n)
    return sum(multiples)