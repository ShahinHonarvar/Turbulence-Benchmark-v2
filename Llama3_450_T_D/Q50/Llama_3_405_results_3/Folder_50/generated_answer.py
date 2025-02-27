def if_contains_anagrams(lst):
    anagram_dict = {}
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word] += 1
            else:
                anagram_dict[sorted_word] = 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_dict.values()))
    return pairs >= 20