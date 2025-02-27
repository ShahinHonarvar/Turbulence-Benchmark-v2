def find_sum_of_multiples(k):
    sum = 0
    for i in range(1, 408):
        sum += k * i
    return sum