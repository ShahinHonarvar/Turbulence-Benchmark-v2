def find_sum_of_multiples(number):
    """
    Returns the sum of the first 45 multiples of the given number.
    """
    sum = 0
    for i in range(1, 46):
        sum += i * number
    return sum