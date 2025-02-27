from functools import partial

def find_original_set():
    arg_sets = set()
    while len(arg_sets) != 194:
        arg_sets.add(input('Enter a set of integers: '))
    return min(arg_sets, key=len)