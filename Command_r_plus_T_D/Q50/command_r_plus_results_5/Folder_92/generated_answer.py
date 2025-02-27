def if_contains_anagrams(words_list):
    anagram_dict = {}
    for word in words_list:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    anagram_pairs = [pair for pair in anagram_dict.values() if len(pair) >= 2]
    return len(anagram_pairs) >= 2