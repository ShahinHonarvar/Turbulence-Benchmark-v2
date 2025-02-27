def if_contains_anagrams(str_list):
    anagram_set = set()
    for str in str_list:
        sorted_str = ''.join(sorted(str.lower()))
        if sorted_str in anagram_set:
            if len(anagram_set) >= 3:
                return False
        else:
            anagram_set.add(sorted_str)
    return True