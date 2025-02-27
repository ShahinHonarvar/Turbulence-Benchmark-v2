def find_sum_of_multiples(n):
    return sum(range(n, 36 * n, n)) if n > 0 else 0