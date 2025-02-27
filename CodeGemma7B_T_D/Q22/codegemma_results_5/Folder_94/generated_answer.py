def find_sum_of_multiples(multi):
    """
    This function takes one argument, a positive integer, and returns the sum of the first
    69 positive multiples of the given integer.
    """
    multiples = []
    for i in range(1, 69):
        multiples.append(i * multi)
    return sum(multiples)