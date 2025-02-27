def find_sum_of_multiples(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError('Argument must be a positive integer')
    sum_of_multiples = 0
    i = 1
    while True:
        multiple = i * n
        if multiple > 2100:
            break
        sum_of_multiples += multiple
        i += 1
    return sum_of_multiples * 2