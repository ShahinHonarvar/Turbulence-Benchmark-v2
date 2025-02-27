from collections import defaultdict

def if_contains_anagrams(words):
    anagram_dict = defaultdict(list)
    for word in words:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_dict[sorted_word].append(word)
    anagram_pairs = 0
    for anagrams in anagram_dict.values():
        if len(anagrams) > 1:
            anagram_pairs += len(anagrams) * (len(anagrams) - 1) // 2
    return anagram_pairs >= 5