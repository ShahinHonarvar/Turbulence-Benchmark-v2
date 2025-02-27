def find_sum_of_multiples(num):
    if num <= 0:
        raise ValueError('Input must be a positive integer')
    sum_of_multiples = 0
    for i in range(1, 50):
        sum_of_multiples += i * num
    return sum_of_multiples