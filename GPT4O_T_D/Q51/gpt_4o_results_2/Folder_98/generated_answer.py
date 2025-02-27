def if_contains_anagrams(strings):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagram_pairs = 0
    sorted_str_dict = {}
    for string in strings:
        if len(string) < 3:
            continue
        sorted_str = sorted_string(string)
        if sorted_str in sorted_str_dict:
            anagram_pairs += sorted_str_dict[sorted_str]
            sorted_str_dict[sorted_str] += 1
        else:
            sorted_str_dict[sorted_str] = 1
        if anagram_pairs > 46:
            return False
    return True