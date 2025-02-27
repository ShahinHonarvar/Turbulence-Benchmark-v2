from collections import Counter

def if_contains_anagrams(strings):
    anagram_counter = Counter()
    for string in strings:
        if len(string) >= 3:
            anagram_counter[''.join(sorted(string.lower()))] += 1
    return sum((count * (count - 1) // 2 for count in anagram_counter.values())) >= 92