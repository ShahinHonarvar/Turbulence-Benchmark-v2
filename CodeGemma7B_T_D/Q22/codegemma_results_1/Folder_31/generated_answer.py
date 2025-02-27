def find_sum_of_multiples(x):
    n = 0
    sum = 0
    while n <= 90:
        n += 1
        sum += x * n
    return sum