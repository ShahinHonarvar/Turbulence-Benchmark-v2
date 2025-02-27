def find_sum_of_multiples(n):
    return sum((i * (i % n == 0) for i in range(1, 402 * n, n)))