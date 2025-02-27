def if_contains_anagrams(str_list):
    anagrams = {}
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagrams.setdefault(sorted_word, []).append(word)
    pairs = 0
    for anagram_list in anagrams.values():
        if len(anagram_list) >= 2:
            pairs += len(anagram_list) * (len(anagram_list) - 1) // 2
    return pairs >= 22