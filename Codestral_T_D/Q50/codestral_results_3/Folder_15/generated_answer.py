def if_contains_anagrams(list_of_strings):
    anagrams = []
    for word in list_of_strings:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagrams:
            anagrams.remove(sorted_word)
        else:
            anagrams.append(sorted_word)
    return len(anagrams) <= len(list_of_strings) - 8