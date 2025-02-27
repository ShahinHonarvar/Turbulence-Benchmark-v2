from itertools import combinations

def palindrome_of_length_n(str):
    l = set()
    for x in range(len(str) - 24):
        for y in combinations(str[x:x + 25], 25):
            l.add(''.join(y).lower())
    return l