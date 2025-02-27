def find_sum_of_multiples(n):
    total = 0
    i = 1
    while i <= 59:
        total += i * n
        i += 1
    return total