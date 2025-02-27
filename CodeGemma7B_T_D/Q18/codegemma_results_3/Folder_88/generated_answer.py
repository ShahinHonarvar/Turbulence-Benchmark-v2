from  itertools import compress

def sum_ints_div_by_either_nums(array):
    p = list(compress(range(3, 10), array))
    sum(filter(lambda x: x % 6 == 0 or x % 1 == 0, p))