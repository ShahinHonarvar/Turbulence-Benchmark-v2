def find_sum_of_multiples(n):
    total = 0
    for x in range(1, 114):
        total += x * n
    return total