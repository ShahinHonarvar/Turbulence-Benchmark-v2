from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            anagrams[str(sorted(word.lower()))].append(word)
    count = 0
    for key in anagrams:
        if len(anagrams[key]) > 1:
            count += len(anagrams[key])
    return count >= 29