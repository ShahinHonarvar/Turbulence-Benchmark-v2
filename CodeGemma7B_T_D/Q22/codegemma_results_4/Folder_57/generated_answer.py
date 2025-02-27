from functools import reduce

def find_sum_of_multiples(num):
    return reduce(lambda a, y=0: a + y, [num * x for x in range(1, 60)])