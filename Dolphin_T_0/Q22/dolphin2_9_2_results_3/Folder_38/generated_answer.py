def find_sum_of_multiples(n):
    summ = 0
    i = 1
    while i < 78:
        summ += n * i
        i += 1
    return summ