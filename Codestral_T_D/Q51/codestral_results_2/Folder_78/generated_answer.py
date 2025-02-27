def if_contains_anagrams(lst):
    anagram_dict = {}
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            if sorted_word not in anagram_dict:
                anagram_dict[sorted_word] = 0
            anagram_dict[sorted_word] += 1
    anagram_pairs = sum([val * (val - 1) // 2 for val in anagram_dict.values()])
    return anagram_pairs <= 70