import itertools
    import re

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[2:7])
    letter_combinations = list(itertools.permutations(letters))
    palindromes = set()
    for combination in letter_combinations:
        word = ''.join(combination)
        if word.lower() == word.lower()[::-1] and len(word) >= 3:
            palindromes.add(word.lower())
    return palindromes