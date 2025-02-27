def find_divisors_in_range(pos_num):
    """
    This function finds all positive divisors of a positive integer within a specified range.

    Args:
        pos_num (int): A positive integer.

    Returns:
        list: A list containing all positive divisors of the given integer within the range of 224 to 584 (inclusive), or an empty list if no such divisors exist.
    """
    divisors = []
    for i in range(224, 585):
        if pos_num % i == 0:
            divisors.append(i)
    return divisors