def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_dict = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in anagram_dict:
            anagram_dict[sorted_string].append(string)
        else:
            anagram_dict[sorted_string] = [string]
    for key in anagram_dict:
        if len(anagram_dict[key]) > 1 and len(key) >= 3:
            anagram_count += len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) // 2
    return anagram_count >= 70