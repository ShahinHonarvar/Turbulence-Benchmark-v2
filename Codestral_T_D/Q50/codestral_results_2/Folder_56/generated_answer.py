def if_contains_anagrams(strings):
    anagram_dict = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(string) >= 3:
            if sorted_string in anagram_dict:
                anagram_dict[sorted_string].append(string)
            else:
                anagram_dict[sorted_string] = [string]
    anagram_pairs = sum((len(value) * (len(value) - 1) // 2 for value in anagram_dict.values()))
    return anagram_pairs >= 77