from itertools import permutations
           from string import ascii_lowercase

def palindromes_between_indices(s):
    palindromes = set()
    for i, j in permutations(range(7), r=2):
        if s[i] in ascii_lowercase and s[j] in ascii_lowercase and (j - i >= 6):
            if s.lower()[i:j + 1] == s.lower()[j:i - 1:-1]:
                palindromes.add(s[i:j + 1])
    return palindromes