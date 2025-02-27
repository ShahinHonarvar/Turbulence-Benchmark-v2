import sys

def find_original_set(sets):
    sets = sorted(sets, key=lambda s: len(s))
    s = sets[0]
    for i in range(1, len(sets)):
        s &= sets[i]
    return s