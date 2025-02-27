from collections import Counter

def if_contains_anagrams(strings):
    anagram_count = Counter()
    for word in strings:
        if len(word) >= 3:
            anagram_count[tuple(sorted(word.lower()))] += 1
    return sum((count * (count - 1) // 2 for count in anagram_count.values())) >= 40