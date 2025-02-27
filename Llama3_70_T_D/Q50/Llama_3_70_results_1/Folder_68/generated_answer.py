def if_contains_anagrams(lst):
    anagram_dict = {}
    for word in lst:
        lower_word = word.lower()
        sorted_word = ''.join(sorted(lower_word))
        if len(word) >= 3:
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(lower_word)
            else:
                anagram_dict[sorted_word] = [lower_word]
    anagram_pairs = 0
    for key in anagram_dict:
        if len(anagram_dict[key]) > 1:
            anagram_pairs += len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) // 2
    return anagram_pairs >= 9