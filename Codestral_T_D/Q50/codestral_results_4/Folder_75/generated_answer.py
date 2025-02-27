def if_contains_anagrams(lst):
    anagram_pairs = 0
    d = {}
    for word in lst:
        if len(word) >= 3:
            key = ''.join(sorted(word.lower()))
            if key not in d:
                d[key] = 1
            else:
                d[key] += 1
                anagram_pairs += d[key]
    return anagram_pairs >= 70