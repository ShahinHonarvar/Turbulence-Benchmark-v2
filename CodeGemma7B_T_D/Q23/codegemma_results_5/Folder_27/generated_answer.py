def find_divisors_in_range(num):
    """
            This function takes a positive integer as its argument, and returns the list of
            all positive divisors of the given integer that are between 15 and 20, both
            inclusive. If no such divisors exist in the specified range, the function
            should return an empty list.
            """
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            if i >= 15 and i <= 20:
                divisors.append(i)
    return divisors