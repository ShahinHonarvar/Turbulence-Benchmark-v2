from collections import defaultdict

def if_contains_anagrams(words):
    anagram_dict = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            normalized = ''.join(sorted(word.lower()))
            anagram_dict[normalized] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_dict.values() if count > 1))
    return anagram_pairs <= 173