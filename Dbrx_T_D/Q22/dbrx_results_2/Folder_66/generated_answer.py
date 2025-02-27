def find_sum_of_multiples(n):
    return sum((i for i in range(n, 26 * n + 1, n)))