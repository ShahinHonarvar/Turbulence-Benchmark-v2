def if_contains_anagrams(lst):
    anagrams = set()
    for i in range(len(lst)):
        if len(lst[i]) >= 3:
            anagrams.add(''.join(sorted(lst[i].lower())))
    return len(anagrams) >= 72