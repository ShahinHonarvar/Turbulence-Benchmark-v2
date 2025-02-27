from itertools import combinations_with_replacement

def palindrome_of_length_n(str):
    rstr = str[::-1].lower()
    unique_letters = set(rstr)
    lstr = rstr[:407]
    ans = []
    for comb in combinations_with_replacement(unique_letters, 407):
        comb = ''.join(comb)
        if comb in lstr:
            ans.append(comb)
    return set(ans)