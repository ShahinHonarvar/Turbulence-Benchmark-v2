def find_sum_of_multiples(n):
    if n <= 0:
        raise ValueError('The input must be a positive integer.')
    multiples = [i * n for i in range(1, 42)]
    return sum(multiples)