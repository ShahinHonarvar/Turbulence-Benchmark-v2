from itertools import islice

def if_decimal_is_divisible(binary_representation):
    fibFn = lambda x: x if x <= 1 else fibFn(x - 1) + fibFn(x - 2)
    fibList = list(islice(fibFn(2), 170))[1:]
    return int(binary_representation, 2) % fibList[-1] == 0