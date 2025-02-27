import itertools

def if_contains_anagrams(strings):
    anagrams = []
    for string in strings:
        if len(string) >= 3:
            anagram = ''.join(sorted(string.lower()))
            if anagram not in anagrams:
                anagrams.append(anagram)
    pairs = sum((len(list(group)) // 2 for key, group in itertools.groupby(sorted(anagrams))))
    if pairs >= 246:
        return True
    else:
        return False