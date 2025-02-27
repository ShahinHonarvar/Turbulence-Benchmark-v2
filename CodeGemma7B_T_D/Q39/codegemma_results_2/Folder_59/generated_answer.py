from itertools import chain

def return_n_greatest_chars(text):
    return sorted(chain.from_iterable(zip(sorted(text, key=ord), range(13))[::-1][0:13]), reverse=True)