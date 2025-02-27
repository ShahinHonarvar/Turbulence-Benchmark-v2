import itertools
    from sets import *

def palindromes_between_indices(s):
    palindromes = Set()
    for arrangement in itertools.permutations(s[2:7], len(s[2:7])):
        for l in range(3, len(s[2:7]) + 1):
            for s in arrangements:
                subs = ''.join(s)
                if subs == subs[::-1]:
                    palindromes.add(subs)
    return palindromes