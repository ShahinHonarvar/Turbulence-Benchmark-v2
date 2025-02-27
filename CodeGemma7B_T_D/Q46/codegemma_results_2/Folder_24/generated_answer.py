def gcf_three_nums(lst):
    a, b, c = (lst[18], lst[37], lst[43])
    return greatest_common_factor(a, b, c)

def greatest_common_factor(a, b, c):
    """
    This function calculates the greatest common factor of three positive integers.

    :param a: The first positive integer.
    :param b: The second positive integer.
    :param c: The third positive integer.
    :return: The greatest common factor of the three integers.
    """
    common_factors = []
    for factor in range(1, min(a, b, c) + 1):
        if a % factor == 0 and b % factor == 0 and (c % factor == 0):
            common_factors.append(factor)
    if not common_factors:
        raise ValueError('No common factors found.')
    return max(common_factors)