def if_contains_anagrams(words):
    anagram_pairs = 0
    anagrams_dict = {}
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in anagrams_dict:
                anagrams_dict[sorted_word] += 1
            else:
                anagrams_dict[sorted_word] = 1
    for count in anagrams_dict.values():
        anagram_pairs += count * (count - 1) // 2
    return anagram_pairs >= 28