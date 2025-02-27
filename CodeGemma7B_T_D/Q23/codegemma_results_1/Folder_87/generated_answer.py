def find_divisors_in_range(number):
    """
            Finds all the divisors in the given range for a given number.

            Args:
              number: The number to find divisors for.

            Returns:
              A list of positive divisors of the given number in the range 50-81, or an empty list if no such divisors exist.
            """
    divisors = []
    for i in range(50, 82):
        if number % i == 0:
            divisors.append(i)
    if divisors:
        return divisors
    else:
        return []