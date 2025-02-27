def if_contains_anagrams(lst):
    anagrams = []
    for word in lst:
        if len(word) >= 3:
            for w in lst:
                if len(w) >= 3 and sorted(w.lower()) == sorted(word.lower()) and (w != word):
                    anagrams.append((word, w))
    return len(anagrams) >= 20