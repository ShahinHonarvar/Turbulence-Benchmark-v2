def find_divisors_in_range(num):
    """
            Finds all positive divisors of a number between 113 and 991, both inclusive.

            Args:
            num: The integer to find divisors for.

            Returns:
            A list of positive divisors between 113 and 991, or an empty list if none exist.
            """
    divisors = []
    for i in range(113, 992):
        if num % i == 0:
            divisors.append(i)
    return divisors