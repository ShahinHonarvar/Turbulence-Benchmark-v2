def find_divisors_in_range(num):
    """Finds all positive divisors of a number in a given range."""
    divisors = []
    for i in range(8, 10):
        if num % i == 0:
            divisors.append(i)
    return divisors