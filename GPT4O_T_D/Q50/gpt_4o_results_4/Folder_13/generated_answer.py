from collections import defaultdict

def if_contains_anagrams(words):
    anagram_count = 0
    word_dict = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            word_dict[sorted_word].append(word)
    for anagram_list in word_dict.values():
        if len(anagram_list) > 1:
            anagram_pairs = len(anagram_list) * (len(anagram_list) - 1) // 2
            anagram_count += anagram_pairs
            if anagram_count >= 144:
                return True
    return False