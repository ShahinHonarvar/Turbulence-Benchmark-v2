def find_divisors_in_range(num):
    """This function finds all positive divisors of num that are between 43 and 77, both inclusive."""
    divisors = []
    for i in range(43, 78):
        if num % i == 0:
            divisors.append(i)
    return divisors