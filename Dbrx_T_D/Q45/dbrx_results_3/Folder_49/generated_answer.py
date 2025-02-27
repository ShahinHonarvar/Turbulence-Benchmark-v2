from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if len(s) < 5:
        return set()
    start, end = (5, 7)
    substr = set(s[start:end + 1])
    substr = substr.intersection(english_letters)
    if not substr:
        return set()
    result = set()
    for i in range(3, len(substr) + 1):
        for combination in itertools.combinations(substr, i):
            combo_str = ''.join(combination)
            if combo_str == combo_str[::-1]:
                result.add(combo_str)
    return result