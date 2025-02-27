def if_contains_anagrams(lst):
    anagram_pairs = 0
    anagram_dict = {}
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word not in anagram_dict:
                anagram_dict[sorted_word] = 1
            else:
                anagram_dict[sorted_word] += 1
    for key in anagram_dict:
        anagram_pairs += anagram_dict[key] * (anagram_dict[key] - 1) // 2
    return anagram_pairs >= 89