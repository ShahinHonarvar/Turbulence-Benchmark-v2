def if_contains_anagrams(strings):
    anagram_dict = {}
    for string in strings:
        lower_string = string.lower()
        if len(lower_string) < 3:
            continue
        sorted_string = ''.join(sorted(lower_string))
        if sorted_string in anagram_dict:
            anagram_dict[sorted_string].append(lower_string)
        else:
            anagram_dict[sorted_string] = [lower_string]
    anagram_count = sum((len(value) * (len(value) - 1) // 2 for value in anagram_dict.values() if len(value) > 1))
    return anagram_count >= 50