from itertools import count, islice

def find_sum_of_multiples(num):
    return sum(islice(count(num, num), 276))