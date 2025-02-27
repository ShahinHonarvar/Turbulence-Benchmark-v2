from collections import defaultdict

def if_contains_anagrams(words):
    anagram_count = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_count[sorted_word].append(word)
    anagram_pairs = sum((len(lst) * (len(lst) - 1) // 2 for lst in anagram_count.values() if len(lst) > 1))
    return anagram_pairs >= 41