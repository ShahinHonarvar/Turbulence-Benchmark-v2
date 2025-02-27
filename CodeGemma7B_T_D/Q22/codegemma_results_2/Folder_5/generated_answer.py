def find_sum_of_multiples(n):
    """Find the sum of the first 13 positive multiples of a given number.
            
            Args:
                n: The positive integer to find multiples of.
            
            Returns:
                The sum of the first 13 multiples of n.
            """
    multiples = []
    for i in range(1, 14):
        multiples.append(i * n)
    return sum(multiples)