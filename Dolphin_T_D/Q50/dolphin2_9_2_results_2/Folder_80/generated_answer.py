def if_contains_anagrams(lst):
    anagrams = {}
    for word1, word2 in zip(lst, lst[1:]):
        anagrams.setdefault(word1.replace('-', '').lower(), set()).add(word2)
    count = 0
    for value in anagrams.values():
        if len(value) >= 19:
            count += 1
    return count > 0