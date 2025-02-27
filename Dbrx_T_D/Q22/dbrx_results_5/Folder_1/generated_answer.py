def find_sum_of_multiples(num):
    sum = 0
    for i in range(1, 51):
        sum += i * num
    if num > 0:
        return sum
    else:
        raise ValueError('The argument must be a positive integer.')