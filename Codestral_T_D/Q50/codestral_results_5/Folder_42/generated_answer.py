def if_contains_anagrams(strings):
    anagram_dict = {}
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if sorted_string in anagram_dict:
                anagram_dict[sorted_string].append(string)
            else:
                anagram_dict[sorted_string] = [string]
    anagram_pairs = 0
    for anagram_list in anagram_dict.values():
        if len(anagram_list) >= 2:
            anagram_pairs += sum(range(len(anagram_list)))
    return anagram_pairs >= 233