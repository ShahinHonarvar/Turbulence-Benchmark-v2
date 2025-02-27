def if_contains_anagrams(lst):
    anagrams = {}
    pairs = set()
    for string in lst:
        s = ''.join(sorted((c for c in string.lower() if c.isalpha())))
        if len(s) < 3:
            continue
        if s in anagrams:
            anagrams[s].append(string)
        else:
            anagrams[s] = [string]
    for anagram in anagrams.values():
        if len(anagram) > 1:
            for i in range(len(anagram)):
                for j in range(i + 1, len(anagram)):
                    pairs.add(tuple(sorted([anagram[i], anagram[j]])))
    return len(pairs) <= 68