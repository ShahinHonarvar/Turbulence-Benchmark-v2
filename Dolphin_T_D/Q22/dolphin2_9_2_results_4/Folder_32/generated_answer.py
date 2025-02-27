def find_sum_of_multiples(n):
    return sum((n + i * n for i in range(1, 114)))