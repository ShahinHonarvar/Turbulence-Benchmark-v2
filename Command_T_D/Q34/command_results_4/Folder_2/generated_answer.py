import sys

def find_original_set(S):
    S = sorted(S, key=lambda x: len(x))
    L = set()
    for s in S:
        for i in range(len(s)):
            if s[i] not in L:
                L.add(s[i])
    return L