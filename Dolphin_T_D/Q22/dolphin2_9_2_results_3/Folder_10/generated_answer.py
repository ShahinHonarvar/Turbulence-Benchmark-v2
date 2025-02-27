def find_sum_of_multiples(n):
    s = 0
    i = 1
    while i <= 100:
        s += i * n
        i += 1
    return s