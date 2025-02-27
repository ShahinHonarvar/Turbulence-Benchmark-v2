def if_contains_anagrams(lst):
    anagram_dict = {}
    count = 0
    for string in lst:
        sorted_string = ''.join(sorted(string.lower()))
        if len(string) >= 3:
            if sorted_string in anagram_dict:
                anagram_dict[sorted_string].append(string)
            else:
                anagram_dict[sorted_string] = [string]
    for key in anagram_dict:
        if len(anagram_dict[key]) >= 2:
            count += len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) // 2
    return count >= 48