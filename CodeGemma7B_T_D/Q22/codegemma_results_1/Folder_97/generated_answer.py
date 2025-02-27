def find_sum_of_multiples(x):
    n = 210 // x
    return sum(range(1, (n + 1) * x, x))