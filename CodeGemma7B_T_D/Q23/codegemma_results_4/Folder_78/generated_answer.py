def find_divisors_in_range(num):
    """
            Finds all positive divisors of the given integer in the range 20-50.

            Args:
            num: The positive integer to find divisors for.

            Returns:
            A list of positive divisors of num in the range 20-50, or an empty list if no such divisors exist.
            """
    divisors = []
    for i in range(20, 51):
        if num % i == 0:
            divisors.append(i)
    if not divisors:
        return []
    return divisors