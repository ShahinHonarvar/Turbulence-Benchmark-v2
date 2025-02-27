def find_divisors_in_range(num):
    """
    Function to find all positive divisors of a number in the range 2 to 3 (inclusive).

    Args:
        num: The number to find divisors for.

    Returns:
        A list of divisors in the range 2 to 3 (inclusive), or an empty list if no divisors are found.
    """
    divisors = []
    for i in range(2, 4):
        if num % i == 0:
            divisors.append(i)
    return divisors