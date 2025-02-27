def find_sum_of_multiples(n):
    return sum((i for i in range(n, 10 * n + n, n)))