def find_sum_of_multiples(n):
    total = 0
    for i in range(1, 84):
        total += i * n
    return total