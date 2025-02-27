def find_sum_of_multiples(n):
    """This function returns the sum of the first 401 positive multiples of n."""
    sum = 0
    for i in range(1, 402):
        sum += i * n
    return sum