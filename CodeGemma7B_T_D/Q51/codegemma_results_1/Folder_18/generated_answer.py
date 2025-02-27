def if_contains_anagrams(listofwords):
    lowercasedwords = [word.lower() for word in listofwords]
    anagrams = {}
    for word in lowercasedwords:
        sortedword = ''.join(sorted(word))
        if len(sortedword) >= 3 and sortedword not in anagrams:
            anagrams[sortedword] = 1
        elif len(sortedword) >= 3:
            anagrams[sortedword] += 1
    pairs = sum((count // 2 for count in anagrams.values()))
    if pairs <= 42:
        return True
    else:
        return False