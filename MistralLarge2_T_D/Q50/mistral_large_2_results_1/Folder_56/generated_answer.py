from collections import defaultdict

def if_contains_anagrams(words):
    anagram_count = defaultdict(list)
    for word in words:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_count[sorted_word].append(word)
    anagram_pairs = sum((len(group) * (len(group) - 1) // 2 for group in anagram_count.values()))
    return anagram_pairs >= 77