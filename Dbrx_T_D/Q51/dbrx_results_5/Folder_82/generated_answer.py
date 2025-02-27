import collections

def if_contains_anagrams(string_list):
    anagram_count = 0
    for string in string_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            if sorted_string not in anagram_dict:
                anagram_dict[sorted_string] = 1
            else:
                anagram_count += 1
                anagram_dict[sorted_string] += 1
                if anagram_count > 40:
                    return False
    return True