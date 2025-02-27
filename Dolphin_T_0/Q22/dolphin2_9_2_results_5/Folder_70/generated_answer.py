def find_sum_of_multiples(n):
    sum = 0
    multiple = n
    for _ in range(1, 402):
        sum += multiple
        multiple += n
    return sum