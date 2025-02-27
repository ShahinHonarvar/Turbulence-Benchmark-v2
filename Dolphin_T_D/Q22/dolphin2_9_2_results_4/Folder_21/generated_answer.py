def find_sum_of_multiples(arg):
    sum = 0
    for i in range(1, 408):
        sum += arg * i
    return sum