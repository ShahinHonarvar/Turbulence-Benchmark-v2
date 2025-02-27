def if_contains_anagrams(lst):
    anagram_dict = {}
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word not in anagram_dict:
                anagram_dict[sorted_word] = [word]
            else:
                anagram_dict[sorted_word].append(word)
    anagram_pairs = sum([len(anagrams) * (len(anagrams) - 1) // 2 for anagrams in anagram_dict.values()])
    return anagram_pairs >= 276