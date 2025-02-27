def find_sum_of_multiples(n):
    total = 0
    i = 0
    while i < 46:
        i += 1
        total += n * i
    return total