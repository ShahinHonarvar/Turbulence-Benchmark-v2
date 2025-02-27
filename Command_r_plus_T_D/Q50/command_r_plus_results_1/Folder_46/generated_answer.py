def if_contains_anagrams(words_list):
    anagram_count = 0
    anagram_dict = {}
    for word in words_list:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word not in anagram_dict:
            anagram_dict[sorted_word] = [word]
        else:
            anagram_dict[sorted_word].append(word)
            anagram_count += len(anagram_dict[sorted_word]) - 1
    anagram_count = sum((1 for v in anagram_dict.values() if len(v) > 1 and len(v[0]) >= 3))
    return anagram_count >= 38