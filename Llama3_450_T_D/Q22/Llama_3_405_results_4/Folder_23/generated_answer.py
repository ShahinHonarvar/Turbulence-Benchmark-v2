def find_sum_of_multiples(n):
    return sum((i for i in range(n, 41 * n + 1, n)))