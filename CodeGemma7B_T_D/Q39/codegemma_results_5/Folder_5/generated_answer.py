from operator import itemgetter

def return_n_greatest_chars(str1):
    return sorted(str1, key=itemgetter(1), reverse=True)[:46]