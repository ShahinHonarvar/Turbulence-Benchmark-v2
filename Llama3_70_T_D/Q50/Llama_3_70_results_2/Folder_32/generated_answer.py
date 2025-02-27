def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for string in lst:
        s = ''.join(sorted(string.lower()))
        if len(string) >= 3 and s in anagrams:
            count += len(anagrams[s])
            anagrams[s].append(string)
        elif len(string) >= 3:
            anagrams[s] = [string]
    return count >= 194