def find_sum_of_multiples(n):
    sum_of_multiples = 0
    i = 1
    while i <= 34:
        sum_of_multiples += n * i
        i += 1
    return sum_of_multiples