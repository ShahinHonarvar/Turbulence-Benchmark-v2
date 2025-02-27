def find_sum_of_multiples(n):
    sum = 0
    i = 0
    while i <= 47:
        sum += i * n
        i += 1
    return sum