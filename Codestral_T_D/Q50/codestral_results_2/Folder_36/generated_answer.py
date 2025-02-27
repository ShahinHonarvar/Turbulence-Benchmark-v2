def if_contains_anagrams(lst):
    anagram_dict = {}
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(word)
            else:
                anagram_dict[sorted_word] = [word]
    anagram_pairs = sum((len(lst) * (len(lst) - 1) // 2 for lst in anagram_dict.values() if len(lst) >= 2))
    return anagram_pairs >= 312