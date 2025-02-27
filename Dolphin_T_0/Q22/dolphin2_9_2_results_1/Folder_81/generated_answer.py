def find_sum_of_multiples(n):
    sum = 0
    i = 1
    while i <= 83:
        sum += n * i
        i += 1
    return sum