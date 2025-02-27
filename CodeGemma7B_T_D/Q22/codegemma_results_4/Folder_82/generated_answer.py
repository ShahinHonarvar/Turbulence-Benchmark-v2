def find_sum_of_multiples(num):
    if num <= 0:
        raise ValueError('Argument num must be positive')
    multiples_sum = 0
    for i in range(1, 34):
        multiples_sum += i * num
    return multiples_sum