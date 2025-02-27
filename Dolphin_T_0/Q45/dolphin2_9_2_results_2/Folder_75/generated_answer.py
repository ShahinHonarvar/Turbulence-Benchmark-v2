from itertools import permutations

def palindromes_between_indices(s):
    subsection = s[2:5].lower()
    palindromes = set()
    for p in permutations(subsection, 3):
        string = ''.join(p)
        if string == string[::-1]:
            palindromes.add(string)
    return palindromes