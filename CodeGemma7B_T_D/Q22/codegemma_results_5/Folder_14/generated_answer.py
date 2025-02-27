def find_sum_of_multiples(n):
    sum = 0
    for i in range(67):
        sum += (i + 1) * n
    return sum