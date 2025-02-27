def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            anagrams[word] = anagrams.get(word, 0) + 1
    if max(anagrams.values(), default=0) > 85:
        return True
    else:
        return False