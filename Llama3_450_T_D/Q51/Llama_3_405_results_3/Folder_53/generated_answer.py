def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        sorted_str = ''.join(sorted(s.lower()))
        if len(sorted_str) < 3:
            continue
        if sorted_str in anagrams and (not anagrams[sorted_str].issubset(set('abcdefghijklmnopqrstuvwxyz'))):
            continue
        if sorted_str not in anagrams:
            anagrams[sorted_str] = set()
        anagrams[sorted_str].add(s.lower())
    count = sum((len(val) * (len(val) - 1) // 2 for val in anagrams.values() if len(val) > 1))
    return count <= 8