def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_dict = {}
    for word in strings:
        lower_word = word.lower()
        if len(lower_word) >= 3:
            sorted_word = ''.join(sorted(lower_word))
            if sorted_word not in anagram_dict:
                anagram_dict[sorted_word] = 0
            anagram_dict[sorted_word] += 1
            anagram_count += anagram_dict[sorted_word] - 1
    return anagram_count >= 35