import collections

def if_contains_anagrams(string_list):
    anagram_count = 0
    for string in string_list:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if collections.Counter(sorted_string) in anagram_dict:
                anagram_count += 1
                anagram_dict[collections.Counter(sorted_string)] += 1
            else:
                anagram_dict[collections.Counter(sorted_string)] = 1
    return anagram_count <= 277