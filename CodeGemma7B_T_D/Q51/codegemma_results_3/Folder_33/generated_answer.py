def if_contains_anagrams(str_list):
    anagram_pairs = {}
    for str in str_list:
        str = ''.join(sorted(str.lower()))
        if len(str) >= 3 and str not in anagram_pairs:
            for other_str in str_list[str_list.index(str) + 1:]:
                if sorted(str) == sorted(other_str.lower()):
                    anagram_pairs[str] = other_str
                    if len(anagram_pairs) > 85:
                        return False
    return True