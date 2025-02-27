def if_contains_anagrams(strings):
    anagram_dict = {}
    for word in strings:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word not in anagram_dict:
                anagram_dict[sorted_word] = 1
            else:
                anagram_dict[sorted_word] += 1
    anagram_pairs = sum((val * (val - 1) // 2 for val in anagram_dict.values()))
    return anagram_pairs >= 84