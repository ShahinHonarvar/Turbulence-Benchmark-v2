from collections import defaultdict

def is_anagram(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

def if_contains_anagrams(words):
    anagram_dict = defaultdict(list)
    for word in words:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_dict[sorted_word].append(word)
    anagram_pairs = 0
    for words in anagram_dict.values():
        n = len(words)
        if n > 1:
            anagram_pairs += n * (n - 1) // 2
    return anagram_pairs <= 72