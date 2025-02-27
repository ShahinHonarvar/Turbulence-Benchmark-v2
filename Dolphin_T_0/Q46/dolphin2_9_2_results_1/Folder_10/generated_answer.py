def gcf_three_nums(lst):
    """
    This function takes a list of positive integers, 'lst', and returns the greatest common factor of the elements at
    indices 86, 89 and 49.

    Args:
        lst: a list of positive integers.

    Returns:
        the greatest common factor of elements at indices 86, 89, and 49.
    """
    num1 = lst[86]
    num2 = lst[89]
    num3 = lst[49]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcd(gcd(num1, num2), num3)