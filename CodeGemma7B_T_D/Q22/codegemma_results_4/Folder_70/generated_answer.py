def find_sum_of_multiples(n):
    total = 0
    i = 0
    while i <= 400:
        total += i * n
        i += 1
    return total