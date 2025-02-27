from collections import defaultdict

def if_contains_anagrams(words):
    anagram_count = 0
    anagrams_dict = defaultdict(list)
    for word in words:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagrams_dict[sorted_word].append(word.lower())
    for anagrams in anagrams_dict.values():
        n = len(anagrams)
        if n > 1:
            anagram_count += n * (n - 1) // 2
    return anagram_count <= 61