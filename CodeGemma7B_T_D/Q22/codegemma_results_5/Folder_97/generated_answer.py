def find_sum_of_multiples(n):
    sum = 0
    for i in range(210):
        sum += n * (i + 1)
    return sum