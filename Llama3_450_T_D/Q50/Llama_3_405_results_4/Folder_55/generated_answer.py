def if_contains_anagrams(strs):
    anagram_dict = {}
    count = 0
    for string in strs:
        sorted_str = ''.join(sorted(string.lower()))
        if len(string) >= 3:
            if sorted_str in anagram_dict:
                anagram_dict[sorted_str].append(string)
            else:
                anagram_dict[sorted_str] = [string]
    for key in anagram_dict:
        if len(anagram_dict[key]) > 1:
            count += len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) // 2
        if count >= 15:
            return True
    return False