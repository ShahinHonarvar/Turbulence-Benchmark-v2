def greatest_common_factor(a, b):
    """
    Returns the greatest common factor of two numbers.
    Args:
        a: The first number.
        b: The second number.
    Returns:
        The greatest common factor of a and b.
    """
    while b > 0:
        a, b = (b, a % b)
    return a