from itertools import combinations_with_replacement

def all_substring_of_size_n(instr):
    return list({''.join(p) for p in combinations_with_replacement(instr, 18)})