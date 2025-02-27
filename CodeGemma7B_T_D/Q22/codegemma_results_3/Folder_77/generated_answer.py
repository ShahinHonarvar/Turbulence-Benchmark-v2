def find_sum_of_multiples(n):
    """Sums the first 173 multiples of n."""
    sum_of_multiples = 0
    for i in range(1, 174):
        sum_of_multiples += i * n
    return sum_of_multiples