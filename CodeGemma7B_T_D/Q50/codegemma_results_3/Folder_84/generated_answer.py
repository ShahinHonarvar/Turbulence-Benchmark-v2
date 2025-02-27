from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    sorted_words = defaultdict(list)
    for word in list_of_strings:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            sorted_words[sorted_word].append(word)
    anagram_pairs = 0
    for word_list in sorted_words.values():
        for i in range(len(word_list)):
            for j in range(i + 1, len(word_list)):
                if len(word_list[i]) == len(word_list[j]):
                    anagram_pairs += 1
    return anagram_pairs >= 108