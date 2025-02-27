def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            anagrams[sorted_word] = anagrams.get(sorted_word, 0) + 1
    return any((count >= 2 for count in anagrams.values()))