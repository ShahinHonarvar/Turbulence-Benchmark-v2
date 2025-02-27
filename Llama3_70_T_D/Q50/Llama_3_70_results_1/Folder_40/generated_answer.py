def if_contains_anagrams(strings):
    anagram_dict = {}
    for string in strings:
        lower_string = string.lower()
        sorted_string = ''.join(sorted(lower_string))
        if len(lower_string) < 3:
            continue
        if sorted_string in anagram_dict:
            anagram_dict[sorted_string].append(string)
        else:
            anagram_dict[sorted_string] = [string]
    count = 0
    for strings in anagram_dict.values():
        count += len(strings) * (len(strings) - 1) // 2
    return count >= 3