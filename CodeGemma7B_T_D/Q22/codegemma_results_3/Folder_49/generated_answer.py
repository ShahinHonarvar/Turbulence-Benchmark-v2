def find_sum_of_multiples(n):
    return sum(filter(lambda x: x % n == 0, range(n, n * 100 + 1, n)))