def find_sum_of_multiples(num):
    """
    This function takes one argument, a positive integer,
    and returns the sum of the first 85 possitive multiples of the given integer.
    """
    sum_of_multiples = 0
    multiples = 85
    for i in range(multiples):
        sum_of_multiples += num * i + num
    return sum_of_multiples