def if_contains_anagrams(strings):
    anagram_dict = {}
    count = 0
    for string in strings:
        normalized = ''.join(sorted(string.lower()))
        if len(normalized) >= 3:
            if normalized in anagram_dict:
                anagram_dict[normalized] += 1
            else:
                anagram_dict[normalized] = 1
    for val in anagram_dict.values():
        if val > 1:
            count += val * (val - 1) // 2
            if count >= 73:
                return True
    return False