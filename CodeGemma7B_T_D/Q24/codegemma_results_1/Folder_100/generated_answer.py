def sum_of_divisors_in_range(n: int) -> int:
    """
    A function that takes a positive integer as its argument, and returns the sum of all positive divisors of the given integer in the range from 11 to 41 inclusive. If no such divisors exist in the specified range, the function should return 0.

    Args:
        n (int): A positive integer.

    Returns:
        int: The sum of all positive divisors of n in range from 11 to 41 inclusive, or 0 if no such divisors exist.
    """
    sum_of_divisors = 0
    for i in range(11, 42):
        if n % i == 0:
            sum_of_divisors += i
    if sum_of_divisors == 0:
        return 0
    return sum_of_divisors