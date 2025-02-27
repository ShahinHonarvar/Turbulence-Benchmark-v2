def if_contains_anagrams(strings):
    anagrams = {}
    anagram_pairs = set()
    for s in strings:
        s = s.lower()
        if len(s) < 3:
            continue
        s = ''.join(filter(str.isalpha, s))
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams:
            for old_s in anagrams[sorted_s]:
                anagram_pairs.add(tuple(sorted([old_s, s])))
            anagrams[sorted_s].append(s)
        else:
            anagrams[sorted_s] = [s]
    return len(anagram_pairs) <= 41