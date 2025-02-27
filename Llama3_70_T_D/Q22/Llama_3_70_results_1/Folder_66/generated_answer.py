def find_sum_of_multiples(n):
    multiples = [i for i in range(n, 25 * n + 1, n)]
    return sum(multiples)