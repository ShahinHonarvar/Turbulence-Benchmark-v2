def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        if len(word) >= 3:
            key = ''.join(sorted(word.lower()))
            if key in anagrams:
                anagrams[key] += 1
            else:
                anagrams[key] = 1
    if_contains = False
    for value in anagrams.values():
        if value >= 2:
            if_contains = True
            break
    return if_contains