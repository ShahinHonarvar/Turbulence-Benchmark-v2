from collections import Counter

def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        if len(word) >= 3:
            key = ''.join(sorted(word.lower()))
            if key not in anagrams:
                anagrams[key] = 1
            else:
                anagrams[key] += 1
    count = sum([1 if anagrams[key] > 1 else 0 for key in anagrams.values()])
    return count >= 44