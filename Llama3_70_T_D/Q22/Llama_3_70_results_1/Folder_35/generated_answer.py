def find_sum_of_multiples(n):
    return sum((i for i in range(n, 116 * n + 1) if i % n == 0))