def find_sum_of_multiples(n):
    sum = 0
    for i in range(1, 86):
        sum += i * n
    return sum