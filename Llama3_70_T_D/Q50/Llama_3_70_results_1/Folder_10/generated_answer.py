def if_contains_anagrams(lst):
    anagram_count = 0
    anagram_dict = {}
    for string in lst:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if sorted_string in anagram_dict:
                anagram_dict[sorted_string].append(string)
            else:
                anagram_dict[sorted_string] = [string]
    for anagrams in anagram_dict.values():
        anagram_count += len(anagrams) * (len(anagrams) - 1) // 2
    return anagram_count >= 52