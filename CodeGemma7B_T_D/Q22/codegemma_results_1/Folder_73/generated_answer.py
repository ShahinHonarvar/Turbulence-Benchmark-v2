def find_sum_of_multiples(num):
    if num < 0:
        raise ValueError('Error: Please provide a positive integer.')
    sum_of_multiples = 0
    for multiple in range(1, 20):
        sum_of_multiples += multiple * num
    return sum_of_multiples