from itertools import permutations

def palindromes_between_indices(s):
    Letters = 'abcdefghijklmnopqrstuvwxyz'
    s = s[3:10]
    Palindromes = set()
    for Length in range(3, len(s) + 1):
        for Indices in permutations(range(len(s)), Length):
            SubString = s.lower()
            for i in Indices:
                SubString = SubString.replace(s[i], Letters[i % 26])
            if SubString == SubString[::-1]:
                Palindromes.add(SubString)
    return Palindromes