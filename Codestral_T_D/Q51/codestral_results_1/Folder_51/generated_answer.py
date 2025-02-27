def if_contains_anagrams(strings):
    anagram_dict = {}
    for string in strings:
        key = ''.join(sorted(string.lower()))
        if key in anagram_dict:
            anagram_dict[key].append(string)
        else:
            anagram_dict[key] = [string]
    total_pairs = 0
    for anagram_list in anagram_dict.values():
        if len(anagram_list) >= 3:
            total_pairs += len(anagram_list) * (len(anagram_list) - 1) // 2
    return total_pairs <= 116