def sum_of_divisors_in_range(number):
    """
    :type number: Positive integer
    :rtype: Integer
    """
    total = 0
    for i in range(451, 974):
        if i % number == 0:
            total += i
    return total