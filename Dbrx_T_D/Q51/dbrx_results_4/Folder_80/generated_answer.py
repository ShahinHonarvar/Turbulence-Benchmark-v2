import collections

def if_contains_anagrams(list_of_strings):
    anagram_count = 0
    for string in list_of_strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if collections.Counter(sorted_string) in anagram_counts:
                anagram_count += 1
            else:
                anagram_counts[collections.Counter(sorted_string)] = 1
    return anagram_count <= 255