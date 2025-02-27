from itertools import combinations

def palindrome_of_length_n(s):
    palindrome = set()
    for c in combinations(s.lower(), 16):
        if c[::6] == c[-7::-1]:
            palindrome.add(''.join(c))
    return palindrome