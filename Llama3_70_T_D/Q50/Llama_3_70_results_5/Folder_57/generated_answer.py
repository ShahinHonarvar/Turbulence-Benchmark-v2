def if_contains_anagrams(lst):
    lst = [x.lower() for x in lst if len(x) >= 3]
    anagrams = {}
    for word in lst:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    pairs = sum([len(words) * (len(words) - 1) // 2 for words in anagrams.values() if len(words) > 1])
    return pairs >= 50