import sys

def find_original_set(S):
    s = set(S)
    s = {e for e in s if len(s) == 1}
    s = {e | {e for s in S for e in s if e == s} for e in s}
    return s