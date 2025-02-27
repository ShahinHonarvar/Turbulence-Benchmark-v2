from itertools import count

def find_sum_of_multiples(multiples):
    return sum((n * multiples for n in count(multiples, multiples)))