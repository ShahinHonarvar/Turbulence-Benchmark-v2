from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        anagrams[sorted_word].append(word)
    anagrams = [value for value in anagrams.values() if len(value) >= 2]
    return len(anagrams) >= 3