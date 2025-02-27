def sum_of_divisors_in_range(number):
    """
            This function calculates the sum of all positive divisors of a given number that lie between 15 and 20.

            Args:
                number: An integer greater than or equal to 1.

            Returns:
                The sum of all positive divisors of the given number that lie between 15 and 20, or 0 if no such divisors exist.
            """
    divisors = []
    for i in range(15, 21):
        if number % i == 0:
            divisors.append(i)
    if not divisors:
        return 0
    else:
        return sum(divisors)