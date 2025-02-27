from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            anagrams[''.join(sorted(word.lower()))].append(word)
    count = 0
    for word, anagram in anagrams.items():
        length = len(anagram)
        if length > 1:
            count += length * (length - 1) // 2
        if count >= 143:
            return True
    return False