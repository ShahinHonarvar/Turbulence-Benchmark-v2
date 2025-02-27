from itertools import permutations

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    substring = s[2:7].lower()
    palindromes = set()
    for combination in permutations(substring, len(substring)):
        combination = ''.join(combination)
        if len(combination) >= 3 and combination == combination[::-1] and set(combination).issubset(english_letters):
            palindromes.add(combination)
    return palindromes