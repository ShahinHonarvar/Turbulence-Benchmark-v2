from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for word in strings:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_dict[sorted_word].append(word)
    anagram_pairs = 0
    for word_list in anagram_dict.values():
        word_count = len(word_list)
        if word_count > 1:
            anagram_pairs += word_count * (word_count - 1) // 2
    return anagram_pairs >= 115