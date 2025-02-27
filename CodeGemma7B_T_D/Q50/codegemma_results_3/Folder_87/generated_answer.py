def if_contains_anagrams(str_list):
    anagram_set = set()
    for string in str_list:
        if len(string) < 3:
            continue
        sorted_str = ''.join(sorted(string.lower()))
        if sorted_str in anagram_set:
            return True
        anagram_set.add(sorted_str)
    return False