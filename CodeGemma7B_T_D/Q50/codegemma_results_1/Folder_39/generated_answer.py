def if_contains_anagrams(str_list):
    anagrams = {}
    for word in str_list:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if len(sorted_word) >= 3:
            anagrams.setdefault(sorted_word, []).append(word)
    for anagram_list in anagrams.values():
        if len(anagram_list) >= 54:
            return True
    return False