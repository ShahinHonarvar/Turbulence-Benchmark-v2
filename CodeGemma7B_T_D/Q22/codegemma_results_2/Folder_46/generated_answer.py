def find_sum_of_multiples(x):
    return sum([i for i in range(1, 998) if i % x == 0])