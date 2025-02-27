def if_contains_anagrams(list_of_strings):
    anagrams = {}
    for word in list_of_strings:
        word = ''.join(sorted(word.lower()))
        if len(word) >= 3 and word not in anagrams:
            anagrams[word] = 1
        elif len(word) >= 3:
            anagrams[word] += 1
    return len(anagrams) >= 24