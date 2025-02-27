from collections import Counter

def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        if len(string) < 3:
            continue
        normalized_string = ''.join(sorted(string.lower()))
        if normalized_string not in anagrams:
            anagrams[normalized_string] = []
        anagrams[normalized_string].append(string)
    for anagram in anagrams.values():
        if len(anagram) > 1:
            anagram_counts = Counter(anagram)
            if sum(anagram_counts.values()) >= 123:
                return True
    return False