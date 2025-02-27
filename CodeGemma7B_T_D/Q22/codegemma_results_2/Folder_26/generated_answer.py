def find_sum_of_multiples(number):
    """
    This function finds the sum of the first 366 positive multiples of the given number.
    """
    sum = 0
    for i in range(1, 367):
        sum += i * number
    return sum