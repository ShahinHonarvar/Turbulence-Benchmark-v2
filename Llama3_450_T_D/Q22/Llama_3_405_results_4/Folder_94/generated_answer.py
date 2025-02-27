def find_sum_of_multiples(n):
    return sum((i for i in range(n, 69 * n + 1, n)))