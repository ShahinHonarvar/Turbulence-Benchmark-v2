def if_contains_anagrams(lst):
    anagrams = set()
    for word in lst:
        if len(word) >= 3:
            word = word.lower()
            anagrams.add(word)
    return len(anagrams) <= 69