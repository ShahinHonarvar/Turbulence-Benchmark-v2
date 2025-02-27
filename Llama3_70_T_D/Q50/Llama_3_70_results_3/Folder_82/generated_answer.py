def if_contains_anagrams(lst):
    lst = [i.casefold() for i in lst if len(i) >= 3]
    anagram_dict = {}
    for string in lst:
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagram_dict:
            anagram_dict[sorted_string].append(string)
        else:
            anagram_dict[sorted_string] = [string]
    anagram_count = sum((len(value) * (len(value) - 1) // 2 for value in anagram_dict.values()))
    return anagram_count >= 276