from collections import Counter

def if_contains_anagrams(strings):
    count = 0
    anagrams = {}
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(sorted_s) >= 3:
            anagram_key = tuple(Counter(sorted_s).items())
            if anagram_key in anagrams:
                count += 1
            else:
                anagrams[anagram_key] = 1
    return count <= 39