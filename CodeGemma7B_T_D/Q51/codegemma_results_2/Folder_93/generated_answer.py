def if_contains_anagrams(lst):
    anagrams = set()
    for word in lst:
        key = ''.join(sorted([c for c in word.lower() if c.isalpha() and len(c) >= 3]))
        anagrams.add(key)
    return len(anagrams) <= 36