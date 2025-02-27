def find_sum_of_multiples(x):
    sum = 0
    i = 1
    while i <= 186:
        sum += i * x
        i += 1
    return sum