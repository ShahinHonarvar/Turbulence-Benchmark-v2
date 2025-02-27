def find_sum_of_multiples(n):
    if n <= 0:
        return None
    sum = 0
    i = 1
    while i <= 3:
        sum += n * i
        i += 1
    return sum