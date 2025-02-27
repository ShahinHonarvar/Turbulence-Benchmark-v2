def find_sum_of_multiples(number):
    if number <= 0:
        raise ValueError('Number must be positive')
    sum = 0
    for i in range(1, 74):
        sum += i * number
    return sum