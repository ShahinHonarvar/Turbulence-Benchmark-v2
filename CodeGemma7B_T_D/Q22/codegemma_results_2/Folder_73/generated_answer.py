def find_sum_of_multiples(n):
    res = 0
    for i in range(1, 20):
        res = res + i * n
    return res