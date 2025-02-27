def find_sum_of_multiples(n):
    """Sum of the first 10 multiples of n."""
    sum_of_multiples = 0
    for i in range(1, 11):
        sum_of_multiples += i * n
    return sum_of_multiples