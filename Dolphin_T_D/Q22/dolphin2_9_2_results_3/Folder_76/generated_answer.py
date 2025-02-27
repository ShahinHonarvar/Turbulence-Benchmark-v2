def find_sum_of_multiples(n):
    sum = 0
    i = 1
    while i <= 257:
        sum += i * n
        i += 1
    return sum