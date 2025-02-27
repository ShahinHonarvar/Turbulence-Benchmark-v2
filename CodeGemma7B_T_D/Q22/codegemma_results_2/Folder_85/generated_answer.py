def find_sum_of_multiples(number):
    """
    This function finds the sum of the first 27 multiples of a given number.
    """
    sum = 0
    for i in range(1, 28):
        sum += i * number
    return sum