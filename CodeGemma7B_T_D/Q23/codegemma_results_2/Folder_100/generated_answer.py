def find_divisors_in_range(target):
    """
    Return list of divisors of target
    within a range of 11 to 41 inclusive.
    """
    result = [i for i in range(11, 42) if target % i == 0]
    return result