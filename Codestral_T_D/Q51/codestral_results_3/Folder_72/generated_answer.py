def if_contains_anagrams(strings):
    anagram_pairs = 0
    anagram_dict = {}
    for string in strings:
        lower_string = string.lower()
        if len(lower_string) < 3:
            continue
        sorted_string = ''.join(sorted(lower_string))
        if sorted_string in anagram_dict:
            anagram_dict[sorted_string].append(string)
        else:
            anagram_dict[sorted_string] = [string]
    for key in anagram_dict:
        anagram_pairs += len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) // 2
    return anagram_pairs <= 188