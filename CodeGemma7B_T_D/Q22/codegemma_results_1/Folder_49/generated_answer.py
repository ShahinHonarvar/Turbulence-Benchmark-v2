def find_sum_of_multiples(n):
    sum = 0
    for i in range(95):
        temp = i + 1
        sum += temp * n
    return sum