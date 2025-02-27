def find_sum_of_multiples(n):
    return sum(list(filter(lambda x: x % n == 0, range(1, 41))))