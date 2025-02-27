def find_sum_of_multiples(n):
    if n < 0:
        return 'Invalid input: Please provide a positive integer'
    else:
        return sum((n * i for i in range(1, 92)))