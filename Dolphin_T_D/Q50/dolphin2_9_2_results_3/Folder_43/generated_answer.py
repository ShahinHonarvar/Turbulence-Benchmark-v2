def if_contains_anagrams(lst):
    anagrams = set()
    for word in lst:
        if len(word) >= 3 and word.lower() != '':
            sorted_word = ''.join(sorted(word.lower()))
            anagrams.add(sorted_word)
    return len(anagrams) >= 61