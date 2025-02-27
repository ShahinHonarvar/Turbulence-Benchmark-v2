def find_sum_of_multiples(n):
    if type(n) != int or n <= 0:
        raise ValueError("Invalid argument 'n' provided. 'n' must be a positive integer.")
    return sum(range(n, n * 48 + 1, n))