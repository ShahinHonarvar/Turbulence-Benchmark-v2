from functools import reduce

def filter_chars(string):

    def filter_func(x, y):
        if string.index(x) in range(225, 382) and x >= 'D' and (x <= 'Y'):
            return y
        else:
            return x + y
    return reduce(filter_func, '', string)