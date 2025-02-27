def if_contains_anagrams(str_list):
    anagram_set = set()
    for string in str_list:
        normalized_string = ''.join(sorted(string.lower()))
        if normalized_string in anagram_set:
            return False
        elif len(normalized_string) >= 3:
            anagram_set.add(normalized_string)
    return True