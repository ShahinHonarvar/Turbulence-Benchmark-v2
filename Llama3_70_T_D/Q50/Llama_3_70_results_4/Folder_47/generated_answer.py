def if_contains_anagrams(strings):
    anagram_dict = {}
    count = 0
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in anagram_dict:
            anagram_dict[sorted_string].append(string)
        else:
            anagram_dict[sorted_string] = [string]
    for key in anagram_dict:
        if len(anagram_dict[key]) > 1:
            count += len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) // 2
    return count >= 47