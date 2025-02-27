def find_sum_of_multiples(num):
    """
    This function takes one argument, a positive integer, and returns the sum of the first 95 possitive multiples of the given integer.

    Parameters
    ----------
    num : int
        a positive integer

    Returns
    -------
    int
        the sum of the first 95 possitive multiples of the given integer
    """
    multiples = 0
    sum = 0
    while multiples < 95:
        multiples += 1
        sum += multiples * num
    return sum