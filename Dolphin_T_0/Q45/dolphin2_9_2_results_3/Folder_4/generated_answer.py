import itertools

def palindromes_between_indices(s):
    s = s[3:10]
    s = ''.join([c for c in s if c.isalpha()]).lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    all_combinations = list(itertools.combinations_with_replacement(s, 7))
    all_combinations = [''.join(c) for c in all_combinations]
    palindromes = set()
    for word in all_combinations:
        if len(set(word) - english_letters) == 0:
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes