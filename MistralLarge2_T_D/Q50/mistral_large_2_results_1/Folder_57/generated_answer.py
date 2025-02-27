from collections import defaultdict

def if_contains_anagrams(words):
    anagram_dict = defaultdict(list)
    for word in words:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_dict[sorted_word].append(word)
    anagram_count = 0
    for word_list in anagram_dict.values():
        if len(word_list) > 1:
            pairs = len(word_list) * (len(word_list) - 1) // 2
            anagram_count += pairs
    return anagram_count >= 50