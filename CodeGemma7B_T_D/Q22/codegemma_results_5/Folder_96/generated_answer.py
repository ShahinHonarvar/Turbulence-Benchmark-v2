def find_sum_of_multiples(x):
    multiples = range(1, 98)
    sum = 0
    for multiple in multiples:
        sum += multiple * x
    return sum