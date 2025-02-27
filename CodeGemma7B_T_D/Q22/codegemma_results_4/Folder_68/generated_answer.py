def find_sum_of_multiples(num):
    if num <= 0:
        raise ValueError('Error: Please provide a valid positive integer')
    multiples = []
    for i in range(1, 5):
        multiples.append(i * num)
    return sum(multiples)