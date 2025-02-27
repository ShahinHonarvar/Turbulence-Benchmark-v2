def find_sum_of_multiples(n):
    sum = 0
    multiple = n
    for i in range(1, 93):
        sum += multiple
        multiple += n
    return sum