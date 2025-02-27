from operator import itemgetter

def return_n_smallest_chars(text):
    return sorted(text, key=itemgetter(0))[:66]