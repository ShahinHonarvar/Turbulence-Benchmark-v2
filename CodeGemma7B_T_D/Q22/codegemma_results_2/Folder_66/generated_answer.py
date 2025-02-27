def find_sum_of_multiples(x):
    """
    sum of multiples of the first 25 elements up to and including x
    """
    n = 1
    current_sum = 0
    while n <= 25:
        current_sum += x * n
        n += 1
    return current_sum