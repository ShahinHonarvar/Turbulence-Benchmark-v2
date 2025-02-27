from collections import Counter

def if_contains_anagrams(strings):
    anagrams = []
    for string in strings:
        string = ''.join(sorted(string.lower()))
        if len(string) >= 3:
            anagrams.append(string)
    anagram_counts = Counter(anagrams)
    return sum((count * (count - 1) // 2 for count in anagram_counts.values())) <= 289