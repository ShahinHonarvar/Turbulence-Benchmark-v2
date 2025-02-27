from itertools import chain

def find_original_set(X):
    S = [set(e) for e in chain.from_iterable(X)]
    S.sort(key=lambda x: (len(x), -len(set(X).intersection(x))))
    return S[0]