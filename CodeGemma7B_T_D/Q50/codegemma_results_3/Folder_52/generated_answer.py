def if_contains_anagrams(list_of_strings):
    list_of_strings = [str.lower().strip() for str in list_of_strings]
    anagrams = {}
    for word in list_of_strings:
        word_sorted = ''.join(sorted(word))
        if word_sorted not in anagrams:
            anagrams[word_sorted] = []
        anagrams[word_sorted].append(word)
    for anagram_list in anagrams.values():
        if len(anagram_list) >= 58 and all((len(a) >= 3 for a in anagram_list)):
            return True
    return False