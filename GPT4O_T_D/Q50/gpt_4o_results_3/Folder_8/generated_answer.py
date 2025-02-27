from collections import defaultdict

def if_contains_anagrams(words):
    word_dict = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            word_dict[sorted_word].append(word)
    anagram_pairs = sum((len(word_list) * (len(word_list) - 1) // 2 for word_list in word_dict.values()))
    return anagram_pairs >= 85