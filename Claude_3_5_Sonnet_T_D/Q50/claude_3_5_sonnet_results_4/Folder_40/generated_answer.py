def if_contains_anagrams(string_list):
    anagram_dict = {}
    anagram_pairs = 0
    for word in string_list:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(word)
            else:
                anagram_dict[sorted_word] = [word]
    for words in anagram_dict.values():
        if len(words) > 1:
            anagram_pairs += len(words) * (len(words) - 1) // 2
    return anagram_pairs >= 3