def if_contains_anagrams(strings):
    anagram_dict = {}
    for string in strings:
        key = ''.join(sorted(string.lower()))
        if len(key) >= 3:
            if key in anagram_dict:
                anagram_dict[key].append(string)
            else:
                anagram_dict[key] = [string]
    anagram_count = sum((len(v) * (len(v) - 1) // 2 for v in anagram_dict.values()))
    return anagram_count >= 209