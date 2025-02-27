from collections import Counter

def if_contains_anagrams(strings):
    anagram_count = Counter()
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagram_count[sorted_string] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return anagram_pairs <= 21