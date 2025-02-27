def find_sum_of_multiples(n):
    return sum((i * n for i in range(1, int(88 * (n + 1) / n) + 1)))