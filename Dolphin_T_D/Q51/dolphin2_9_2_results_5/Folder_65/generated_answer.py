def if_contains_anagrams(string_list):
    anagram_pairs = 0
    anagram_dict = {}
    for string in string_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            if sorted_string in anagram_dict:
                anagram_dict[sorted_string] += 1
                anagram_pairs += 1
            else:
                anagram_dict[sorted_string] = 1
    return anagram_pairs <= 72