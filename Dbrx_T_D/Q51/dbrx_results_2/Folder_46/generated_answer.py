import collections

def if_contains_anagrams(string_list):
    anagram_count = 0
    for string in string_list:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if collections.Counter(sorted_string) in anagram_count:
                anagram_count[collections.Counter(sorted_string)] += 1
                if anagram_count[collections.Counter(sorted_string)] > 2:
                    return True
            else:
                anagram_count[collections.Counter(sorted_string)] = 1
    return False