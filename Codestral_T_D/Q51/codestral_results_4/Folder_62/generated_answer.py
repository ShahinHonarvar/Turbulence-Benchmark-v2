def if_contains_anagrams(strings):
    anagram_dict = {}
    for word in strings:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagram_dict[sorted_word] = anagram_dict.get(sorted_word, 0) + 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_dict.values()))
    return anagram_pairs <= 289