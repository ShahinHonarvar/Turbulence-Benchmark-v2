from itertools import combinations_with_replacement

def palindrome_of_length_at_least_n(word):
    WORD = word.upper()
    D = {}
    for k in range(10, 26 + 1):
        for cmb in combinations_with_replacement(WORD, k):
            val = ''.join(cmb)
            if val == val[::-1]:
                D[val] = 1
    return set(D.keys())