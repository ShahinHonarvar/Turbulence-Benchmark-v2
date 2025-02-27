def sum_of_divisors_in_range(num):
    """
                    This function returns the sum of all positive divisors of a given integer
                    that are between 451 and 973, both inclusive.

                    Args:
                        num: The integer to find the divisors of.

                    Returns:
                        The sum of all positive divisors of the given integer that are between 451 and 973, both inclusive.
                    """
    sum_of_divisors = 0
    for i in range(451, 974):
        if num % i == 0:
            sum_of_divisors += i
    if sum_of_divisors == 0:
        return 0
    else:
        return sum_of_divisors