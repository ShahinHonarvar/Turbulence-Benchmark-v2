def find_divisors_in_range(number):
    """
    Returns the list of all positive divisors of the given integer that are between 27 and 44, both inclusive. If no such divisors exist in the specified range, the function should return an empty list.
    """
    divisors = []
    for i in range(27, 45):
        if number % i == 0:
            divisors.append(i)
    if divisors == []:
        return []
    return divisors