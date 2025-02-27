def if_contains_anagrams(string_list):

    def sorted_chars(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = {}
    for string in string_list:
        if len(string) >= 3:
            sorted_string = sorted_chars(string)
            if sorted_string in anagram_dict:
                anagram_dict[sorted_string] += 1
            else:
                anagram_dict[sorted_string] = 1
    anagram_pairs = 0
    for count in anagram_dict.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
    return anagram_pairs >= 64