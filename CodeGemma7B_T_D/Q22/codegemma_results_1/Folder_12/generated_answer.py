def find_sum_of_multiples(num):
    if num <= 0:
        raise ValueError('The given number must be a positive integer')
    for n in range(1, 86):
        if num % n == 0:
            multiples_list.append(num)
    return multiples_list