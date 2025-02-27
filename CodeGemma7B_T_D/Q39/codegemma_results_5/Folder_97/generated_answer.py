import operator

def return_n_greatest_chars(s):
    result = sorted(s, key=operator.attrgetter('__contains__', '__ne__'), reverse=True)
    return result[:38]