def find_sum_of_multiples(n):
    return sum((i for i in range(n, n * 402) if i % n == 0))