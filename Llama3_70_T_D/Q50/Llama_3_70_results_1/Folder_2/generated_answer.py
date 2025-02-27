def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for string in strings:
        string_lower = string.lower()
        if len(string_lower) < 3:
            continue
        string_sorted = ''.join(sorted(string_lower))
        if string_sorted in anagrams:
            anagrams[string_sorted].append(string)
        else:
            anagrams[string_sorted] = [string]
    for anagram_list in anagrams.values():
        count += len(anagram_list) * (len(anagram_list) - 1) // 2
    return count >= 246