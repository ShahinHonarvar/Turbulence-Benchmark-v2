def find_sum_of_multiples(n):
    total_sum = 0
    for i in range(1, 38):
        current = n * i
        total_sum += current
    return total_sum