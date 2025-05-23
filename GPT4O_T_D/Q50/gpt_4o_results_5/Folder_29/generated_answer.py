from collections import defaultdict

def if_contains_anagrams(words):
    anagram_dict = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_dict[sorted_word].append(word)
    anagram_pairs_count = 0
    for word_list in anagram_dict.values():
        if len(word_list) > 1:
            anagram_pairs_count += len(word_list) * (len(word_list) - 1) // 2
            if anagram_pairs_count >= 35:
                return True
    return False