def if_contains_anagrams(strings):
    anagrams_count = 0
    strings_set = set()
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) < 3:
            continue
        sorted_s = ''.join(sorted(s_lower))
        if sorted_s in strings_set:
            anagrams_count += 1
        strings_set.add(sorted_s)
    return anagrams_count >= 189