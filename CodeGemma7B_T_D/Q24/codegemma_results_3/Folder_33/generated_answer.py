def sum_of_divisors_in_range(num):
    """
    Adds together all of the positive divisors of the argument that are between 157 and 902, inclusive.
    """
    sum = 0
    for i in range(157, 903):
        if num % i == 0:
            sum += i
    return sum