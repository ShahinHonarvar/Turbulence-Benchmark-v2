import sys

def find_original_set(S):
    S.sort(key=lambda x: len(x))
    s = set()
    for i in range(len(S)):
        s.update(S[i])
    return s