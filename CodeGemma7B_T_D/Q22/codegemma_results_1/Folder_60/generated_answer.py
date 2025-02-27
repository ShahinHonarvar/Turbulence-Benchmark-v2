def find_sum_of_multiples(n):
    """Finds the sum of the first 35 multiples of a given integer.

            Args:
                n: The integer to find multiples of.

            Returns:
                The sum of the first 35 multiples of n.
            """
    multiples = []
    for i in range(1, 36):
        multiple = i * n
        multiples.append(multiple)
    return sum(multiples)