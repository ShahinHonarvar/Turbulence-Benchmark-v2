def if_contains_anagrams(lst):
    anagram_dict = {}
    for word in lst:
        lower_word = word.lower()
        if len(lower_word) >= 3:
            sorted_word = ''.join(sorted(lower_word))
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(lower_word)
            else:
                anagram_dict[sorted_word] = [lower_word]
    anagram_count = sum((len(words) * (len(words) - 1) // 2 for words in anagram_dict.values() if len(words) > 1))
    return anagram_count >= 19