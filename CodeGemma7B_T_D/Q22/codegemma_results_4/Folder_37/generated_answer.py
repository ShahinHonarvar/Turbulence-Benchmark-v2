def find_sum_of_multiples(x):
    return sum((i for i in range(1, 17 * x + 1, x)))