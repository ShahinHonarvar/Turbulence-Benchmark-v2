import collections

def if_contains_anagrams(strings):
    count = 0
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if sorted_string in anagram_dict:
                if anagram_dict[sorted_string] == 1:
                    count += 1
                anagram_dict[sorted_string] += 1
            else:
                anagram_dict[sorted_string] = 1
    return count <= 401