from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:4].lower()
    palindromes = {s[i:j] for i in range(len(s)) for j in range(i + 3, len(s) + 1) if s[i:j] == s[i:j][::-1]}
    return palindromes