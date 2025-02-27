def if_contains_anagrams(lst):
    anagram_map = {}
    for string in lst:
        lower_string = string.lower()
        sorted_string = ''.join(sorted(lower_string))
        if len(lower_string) >= 3:
            if sorted_string in anagram_map:
                anagram_map[sorted_string].append(lower_string)
            else:
                anagram_map[sorted_string] = [lower_string]
    count = 0
    for anagrams in anagram_map.values():
        count += len(anagrams) * (len(anagrams) - 1) // 2
    return count >= 86