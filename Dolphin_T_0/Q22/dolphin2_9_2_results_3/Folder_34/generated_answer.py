def find_sum_of_multiple(n):
    sum = 0
    for i in range(1, 25):
        sum += i * n
    return sum