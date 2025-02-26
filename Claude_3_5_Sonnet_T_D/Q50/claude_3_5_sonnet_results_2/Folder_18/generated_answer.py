from collections import Counter

def if_contains_anagrams(string_list):
    anagram_count = 0
    word_dict = {}
    for word in string_list:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word in word_dict:
                word_dict[sorted_word].append(word)
            else:
                word_dict[sorted_word] = [word]
    for anagram_group in word_dict.values():
        if len(anagram_group) > 1:
            anagram_count += sum(range(len(anagram_group)))
    return anagram_count >= 106