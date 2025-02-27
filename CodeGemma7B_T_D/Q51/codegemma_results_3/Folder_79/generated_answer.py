def if_contains_anagrams(str_list):
    anagram_set = set()
    for string in str_list:
        sorted_str = ''.join(sorted(string.lower()))
        if len(sorted_str) >= 3:
            anagram_set.add(sorted_str)
    return len(anagram_set) <= 173