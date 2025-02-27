def find_sum_of_multiples(a):
    sum = 0
    for i in range(1, 91):
        sum += i * a
    return sum