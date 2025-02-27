def if_contains_anagrams(words_list):
    anagram_count = 0
    words_set = {word.lower() for word in words_list if len(word) >= 3}
    for word in words_set:
        sorted_word = ''.join(sorted(word))
        anagram_group = [w for w in words_set if sorted(w) == sorted_word]
        if len(anagram_group) > 1:
            anagram_count += len(anagram_group) * (len(anagram_group) - 1)
    return anagram_count >= 66