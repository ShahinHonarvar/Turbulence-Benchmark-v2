def find_sum_of_multiples(n):
    return sum((i for i in range(1, 7) for _ in range(n) if i % n == 0))