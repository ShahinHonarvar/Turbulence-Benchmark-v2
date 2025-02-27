def if_contains_anagrams(strings):
    anagram_dict = {}
    count = 0
    for string in strings:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            if sorted_str in anagram_dict:
                anagram_dict[sorted_str].append(string)
            else:
                anagram_dict[sorted_str] = [string]
    for key in anagram_dict:
        count += len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) // 2
    return count >= 312