def find_sum_of_multiples(n):
    return sum((i for i in range(n, 277 * n) if i % n == 0))