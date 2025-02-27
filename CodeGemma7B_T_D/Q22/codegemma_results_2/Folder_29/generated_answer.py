def find_sum_of_multiples(arg):
    return sum((i for i in range(1, 95) if i % arg == 0))