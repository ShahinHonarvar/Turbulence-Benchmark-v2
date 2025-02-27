def find_divisors_in_range(num):
    """Returns a list of positive divisors of num that are between 372 and 494, both inclusive. Returns an empty list if no such divisors exist."""
    divisors = []
    for i in range(372, 496):
        if num % i == 0:
            divisors.append(i)
    return divisors