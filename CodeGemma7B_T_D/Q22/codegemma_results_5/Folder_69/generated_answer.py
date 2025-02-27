def find_sum_of_multiples(x):
    sum = 0
    for n in range(1, 473):
        sum += n * x
    return sum