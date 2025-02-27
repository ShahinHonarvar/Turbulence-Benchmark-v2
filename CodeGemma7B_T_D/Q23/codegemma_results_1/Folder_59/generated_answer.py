def find_divisors_in_range(n):
    """
            Finds all positive divisors of a given integer in range [3, 5].

            Args:
                n: The integer to find divisors for.

            Returns:
                A list of divisors between 3 and 5, inclusive, or an empty list if no such divisors exist.
            """
    divisors = []
    for i in range(3, 6):
        if n % i == 0:
            divisors.append(i)
    return divisors