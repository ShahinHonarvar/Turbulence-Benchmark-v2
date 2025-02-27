def find_sum_of_multiples(n):
    total = 0
    i = 1
    while i * n <= 94:
        total += i * n
        i += 1
    return total