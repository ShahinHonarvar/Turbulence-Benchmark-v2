def sum_of_divisors_in_range(n):
    """
            This function takes a positive integer as its argument, and returns the sum of all
            positive divisors of the given integer that are between 1 and 9, both inclusive. If
            no such divisors exist in the specified range, the function should return 0.
            """
    divs = []
    for i in range(1, 10):
        if n % i == 0:
            divs.append(i)
    return sum(divs) if divs else 0