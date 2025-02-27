def find_sum_of_multiples(i):
    sum = 0
    for x in range(1, 28):
        sum = sum + i * x
    return sum