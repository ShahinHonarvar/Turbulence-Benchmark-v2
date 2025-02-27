def find_divisors_in_range(n):
    """
    Finds the divisors of a number in a specified range.

    Params:
        n (int): The number to find divisors of.

    Returns:
        list: The list of divisors in the range.
    """
    divisors = []
    for i in range(15, 93):
        if i % n == 0:
            divisors.append(i)
    return divisors if divisors else []