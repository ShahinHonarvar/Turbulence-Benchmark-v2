def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        if len(word) < 3:
            continue
        key = ''.join(sorted(word.lower()))
        if key in anagrams:
            anagrams[key].append(word)
        else:
            anagrams[key] = [word]
    anagram_pairs = sum((len(v) * (len(v) - 1) // 2 for v in anagrams.values()))
    return anagram_pairs >= 41