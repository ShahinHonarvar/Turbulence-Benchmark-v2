def find_sum_of_multiples(arg):
    sum = 0
    for i in range(64):
        sum += (i + 1) * arg
    return sum