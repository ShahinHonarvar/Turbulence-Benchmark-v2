def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_dict = {}
    for word in strings:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    for anagrams in anagram_dict.values():
        if len(anagrams) >= 3:
            anagram_count += len(anagrams) * (len(anagrams) - 1) // 2
    return anagram_count >= 43