def find_sum_of_multiples(n):
    if n <= 0:
        raise ValueError('Number must be greater than 0')
    return sum([i * n for i in range(1, 38)])