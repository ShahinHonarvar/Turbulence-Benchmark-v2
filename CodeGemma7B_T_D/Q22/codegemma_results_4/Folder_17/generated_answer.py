def find_sum_of_multiples(n):
    limit = n * 289
    multiples = [i for i in range(n, limit + 1, n)]
    return sum(multiples)