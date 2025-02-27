from collections import defaultdict

def if_contains_anagrams(words):
    anagram_dict = defaultdict(list)
    for word in words:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_dict[sorted_word].append(word)
    anagram_count = 0
    for words in anagram_dict.values():
        if len(words) > 1:
            anagram_count += len(words) - 1
    return anagram_count >= 41