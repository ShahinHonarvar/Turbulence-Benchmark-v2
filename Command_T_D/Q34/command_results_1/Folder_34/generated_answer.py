import sys

def find_original_set(s):
    s.sort()
    sets = set()
    stk = []
    for x in s:
        if x not in stk:
            sets.add(x)
            stk.append(x)
        else:
            pass
    return sets