def find_sum_of_multiples(multiple):
    if multiple <= 0:
        raise ValueError('Argument must be a positive integer')
    return sum(range(multiple, 13 * multiple + 1, multiple))