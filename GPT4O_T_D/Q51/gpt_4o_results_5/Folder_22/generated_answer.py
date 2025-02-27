def if_contains_anagrams(strings):
    anagram_dict = {}
    count = 0
    for string in strings:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            if sorted_str in anagram_dict:
                count += anagram_dict[sorted_str]
                if count > 14:
                    return False
                anagram_dict[sorted_str] += 1
            else:
                anagram_dict[sorted_str] = 1
    return True