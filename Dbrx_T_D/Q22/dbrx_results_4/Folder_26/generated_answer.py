from functools import reduce

def find_sum_of_multiples(num):
    return reduce(lambda x, _: x + _, range(1, 367)) * num