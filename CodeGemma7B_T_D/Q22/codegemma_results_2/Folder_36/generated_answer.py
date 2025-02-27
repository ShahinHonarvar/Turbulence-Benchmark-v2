def find_sum_of_multiples(n):
    result = sum((i * n for i in range(1, 339)))
    return result