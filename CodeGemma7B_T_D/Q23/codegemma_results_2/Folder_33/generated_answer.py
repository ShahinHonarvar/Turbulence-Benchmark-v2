def find_divisors_in_range(num):
    """
    This function takes a positive integer as its argument and returns the list of all positive divisors of the given integer that are between 157 and 902, both inclusive. If no such divisors exist in the specified range, the function should return an empty list.
    """
    divisors = [i for i in range(1, num + 1) if num % i == 0 and 157 <= i <= 902]
    return divisors