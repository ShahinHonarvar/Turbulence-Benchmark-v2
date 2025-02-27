def find_sum_of_multiples(multiple):
    return sum((i for i in range(1, 42) if i % multiple == 0))