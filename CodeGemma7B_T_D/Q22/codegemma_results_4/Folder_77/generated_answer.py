def find_sum_of_multiples(num):
    """
            Function to find the sum of the first 173 multiples
            of a given integer.
            """
    sum = 0
    for i in range(1, 174):
        sum = sum + i * num
    return sum