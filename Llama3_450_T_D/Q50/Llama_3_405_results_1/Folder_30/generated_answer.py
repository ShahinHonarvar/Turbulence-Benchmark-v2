def if_contains_anagrams(strings):
    anagram_count = 0
    sorted_strings = {}
    for s in strings:
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s.lower()))
        if sorted_str in sorted_strings:
            anagram_count += sorted_strings[sorted_str]
            sorted_strings[sorted_str] += 1
        else:
            sorted_strings[sorted_str] = 1
    return anagram_count >= 78