from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    pairs = set()
    for word in lst:
        if len(word) >= 3 and all((c.isalpha() or c.isspace() for c in word)):
            lower_word = word.lower()
            sorted_word = ''.join(sorted(lower_word))
            pairs.add((sorted_word, lower_word))
    if len(pairs) > 55:
        return False
    return True