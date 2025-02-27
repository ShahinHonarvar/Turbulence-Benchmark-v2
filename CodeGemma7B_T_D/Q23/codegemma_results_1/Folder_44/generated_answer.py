def find_divisors_in_range(number):
    """
            Finds all positive divisors of the given number that are between 50 and 84, both inclusive.

            Args:
                number: The positive integer to find divisors of.

            Returns:
                A list of all positive divisors of the given number that are between 50 and 84, both inclusive. If no such divisors exist in the specified range, the function should return an empty list.
            """
    divisors = []
    for i in range(50, 85):
        if number % i == 0:
            divisors.append(i)
    return divisors