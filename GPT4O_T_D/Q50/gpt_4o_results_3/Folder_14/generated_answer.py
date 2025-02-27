def if_contains_anagrams(strings):
    anagram_dict = {}
    for s in strings:
        normalized = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            if normalized in anagram_dict:
                anagram_dict[normalized] += 1
            else:
                anagram_dict[normalized] = 1
    count = 0
    for occurrence in anagram_dict.values():
        if occurrence > 1:
            count += occurrence * (occurrence - 1) // 2
        if count >= 22:
            return True
    return False