def if_contains_anagrams(lst):
    anagram_dict = {}
    for word in lst:
        lower_word = word.lower()
        if len(lower_word) >= 3:
            sorted_word = ''.join(sorted(lower_word))
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word] += 1
            else:
                anagram_dict[sorted_word] = 1
    anagram_pairs = sum((val * (val - 1) // 2 for val in anagram_dict.values()))
    return anagram_pairs <= 416