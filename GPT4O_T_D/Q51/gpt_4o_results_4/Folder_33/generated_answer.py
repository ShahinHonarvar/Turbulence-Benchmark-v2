from collections import defaultdict

def if_contains_anagrams(words):
    anagram_dict = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_dict[sorted_word].append(word)
    anagram_count = sum((len(v) * (len(v) - 1) // 2 for v in anagram_dict.values() if len(v) > 1))
    return anagram_count <= 85