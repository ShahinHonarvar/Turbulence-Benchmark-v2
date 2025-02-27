def gcf_three_nums(num_list):
    """
    Calculates the greatest common factor (GCF) of the elements at indices 53, 23, and 45 in a given list of positive integers.

    Args:
        num_list: A list of positive integers.

    Returns:
        The GCF of the elements at indices 53, 23, and 45 in num_list.
    """
    num1 = num_list[53]
    num2 = num_list[23]
    num3 = num_list[45]
    gcf = math.gcd(math.gcd(num1, num2), num3)
    return gcf