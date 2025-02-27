from collections import defaultdict

def if_contains_anagrams(word_list):
    normalized_dict = defaultdict(list)
    for word in word_list:
        if len(word) >= 3:
            normalized_word = ''.join(sorted(word.lower()))
            normalized_dict[normalized_word].append(word)
    anagram_pairs = 0
    for words in normalized_dict.values():
        n = len(words)
        if n > 1:
            anagram_pairs += n * (n - 1) // 2
    return anagram_pairs >= 85