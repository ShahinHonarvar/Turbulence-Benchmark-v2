def find_sum_of_multiples(n):
    return sum((i for i in range(n, 68 * n + 1, n)))