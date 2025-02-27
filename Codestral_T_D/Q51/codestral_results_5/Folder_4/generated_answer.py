def if_contains_anagrams(words):
    anagram_count = 0
    anagram_dict = {}
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) < 3:
            continue
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    for anagrams in anagram_dict.values():
        if len(anagrams) > 1:
            anagram_count += len(anagrams) * (len(anagrams) - 1) // 2
    return anagram_count <= 84