def find_sum_of_multiples(n):
    total_sum = 0
    for i in range(1, 408):
        total_sum += n * i
    return total_sum