def find_sum_of_multiples(x):
    sum = 0
    i = 0
    while i < 16:
        i += 1
        sum += x * i
    return sum