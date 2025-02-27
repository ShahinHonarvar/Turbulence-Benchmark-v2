def find_sum_of_multiples(n):
    sum_multiples = 0
    for i in range(1, 100):
        multiple = i * n
        if multiple % 2 == 0 or multiple % 5 == 0:
            sum_multiples += multiple
    return sum_multiples