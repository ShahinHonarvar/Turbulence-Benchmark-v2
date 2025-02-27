def find_sum_of_multiples(n):
    sum = 0
    for i in range(1, 5):
        multiple = i * n
        sum += multiple
    return sum