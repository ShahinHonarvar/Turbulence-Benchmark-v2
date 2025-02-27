def find_sum_of_multiples(x):
    sum_of_mul = 0
    for i in range(1, 206):
        if i % x == 0:
            sum_of_mul += i
    return sum_of_mul