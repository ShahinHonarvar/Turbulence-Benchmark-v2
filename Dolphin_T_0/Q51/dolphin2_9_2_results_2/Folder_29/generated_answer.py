from collections import Counter

def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagrams[sorted_word] = anagrams.get(sorted_word, Counter())
        anagrams[sorted_word].update(lst.count(word))
    for count in anagrams.values():
        if count > 318:
            return False
    return True