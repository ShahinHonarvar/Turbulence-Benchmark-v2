def find_sum_of_multiples(n):
    sum = 0
    for i in range(1, 48):
        sum += n * i
    return sum