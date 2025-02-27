def find_sum_of_multiples(n):
    s = sum((n * k for k in range(1, 57)))
    return s