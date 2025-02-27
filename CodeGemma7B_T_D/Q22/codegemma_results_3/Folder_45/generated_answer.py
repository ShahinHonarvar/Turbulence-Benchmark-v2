def find_sum_of_multiples(n):
    a = 0
    for i in range(1, 73):
        a += i * n
    return a