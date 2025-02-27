def if_contains_anagrams(strings):
    anagram_dict = {}
    for word in strings:
        lower_word = word.lower()
        if len(lower_word) >= 3:
            sorted_word = ''.join(sorted(lower_word))
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(lower_word)
            else:
                anagram_dict[sorted_word] = [lower_word]
    anagram_pairs = sum((len(val) * (len(val) - 1) // 2 for val in anagram_dict.values()))
    return anagram_pairs >= 96