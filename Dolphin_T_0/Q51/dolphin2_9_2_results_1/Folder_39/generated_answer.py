def if_contains_anagrams(list_of_strings):
    anagram_dict = {}
    for string in list_of_strings:
        key = ''.join(sorted(string.lower()))
        if len(key) >= 3:
            if key not in anagram_dict:
                anagram_dict[key] = [string]
            else:
                anagram_dict[key].append(string)
    pairs_of_anagrams = 0
    for value in anagram_dict.values():
        if len(value) > 1:
            pairs_of_anagrams += 1
    return pairs_of_anagrams <= 257