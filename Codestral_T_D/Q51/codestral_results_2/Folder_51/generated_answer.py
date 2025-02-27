def if_contains_anagrams(words):
    anagram_count = 0
    anagram_dict = {}
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            if sorted_word in anagram_dict:
                anagram_count += 1
            anagram_dict[sorted_word] = anagram_dict.get(sorted_word, 0) + 1
    return anagram_count <= 116