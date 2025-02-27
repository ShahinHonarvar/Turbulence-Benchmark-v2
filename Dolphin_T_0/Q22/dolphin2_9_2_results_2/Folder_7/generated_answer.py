def find_sum_of_multiples(n):
    if n < 0:
        return 'Input must be a positive integer'
    else:
        return sum((n * i for i in range(1, 417)))