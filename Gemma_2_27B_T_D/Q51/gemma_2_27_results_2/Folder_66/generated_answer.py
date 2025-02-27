from collections import Counter

def if_contains_anagrams(words):
    anagram_counts = {}
    for word in words:
        if len(word) >= 3:
            key = ''.join(sorted(word.lower()))
            if key in anagram_counts:
                anagram_counts[key] += 1
            else:
                anagram_counts[key] = 1
    return sum((count * (count - 1) // 2 for count in anagram_counts.values())) <= 64