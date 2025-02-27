def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) < 3:
            continue
        sorted_str = ''.join(sorted(s_lower))
        if sorted_str in anagrams:
            anagrams[sorted_str].append(s_lower)
        else:
            anagrams[sorted_str] = [s_lower]
    for anagram_list in anagrams.values():
        count += len(anagram_list) * (len(anagram_list) - 1) // 2
    return count >= 41