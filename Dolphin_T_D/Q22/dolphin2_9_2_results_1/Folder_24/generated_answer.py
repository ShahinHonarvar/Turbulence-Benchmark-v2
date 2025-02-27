def find_sum_of_multiples(n):
    if n < 1:
        raise ValueError('The value must be a positive integer.')
    sum_multiples = 0
    for i in range(1, 50):
        sum_multiples += n * i
    return sum_multiples