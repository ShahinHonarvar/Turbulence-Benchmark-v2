def find_sum_of_multiples(number):
    """
    This function finds the sum of the first 92 positive multiples of the given integer.
    """
    sum = 0
    for i in range(1, 93):
        sum += number * i
    return sum