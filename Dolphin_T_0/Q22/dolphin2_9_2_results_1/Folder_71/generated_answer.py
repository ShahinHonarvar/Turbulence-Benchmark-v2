def find_sum_of_multiples(n):
    if n < 1:
        raise ValueError('Input should be a positive integer')
    return sum((n * i for i in range(1, 17)))