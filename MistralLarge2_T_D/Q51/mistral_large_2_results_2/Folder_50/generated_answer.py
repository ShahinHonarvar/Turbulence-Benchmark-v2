from collections import defaultdict

def is_anagram(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

def if_contains_anagrams(words):
    anagram_count = 0
    seen = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            seen[sorted_word].append(word)
    for group in seen.values():
        if len(group) > 1:
            anagram_count += len(group) * (len(group) - 1) // 2
    return anagram_count <= 47