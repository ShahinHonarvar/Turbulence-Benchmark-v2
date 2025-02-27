def find_divisors_in_range(number: int) -> list[int]:
    """
    This function takes a positive integer as its argument, and returns the list of all positive divisors of the given integer that are between 32 and 35, both inclusive. If no such divisors exist in the specified range, the function should return an empty list.
    """
    divisors = []
    for divisor in range(32, 36):
        if number % divisor == 0:
            divisors.append(divisor)
    return divisors