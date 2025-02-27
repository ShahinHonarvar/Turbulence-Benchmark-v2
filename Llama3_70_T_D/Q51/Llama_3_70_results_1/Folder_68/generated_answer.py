def if_contains_anagrams(strings):
    anagram_dict = {}
    count = 0
    for string in strings:
        lower_string = string.lower()
        if len(lower_string) >= 3:
            key = ''.join(sorted(lower_string))
            if key in anagram_dict:
                anagram_dict[key] += 1
            else:
                anagram_dict[key] = 1
    for key in anagram_dict:
        count += anagram_dict[key] * (anagram_dict[key] - 1) // 2
    return count <= 94