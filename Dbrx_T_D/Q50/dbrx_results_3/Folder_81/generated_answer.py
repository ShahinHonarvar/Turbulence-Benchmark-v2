import collections

def if_contains_anagrams(list_of_strings):
    anagrams_count = 0
    anagrams_map = {}
    for string in list_of_strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if sorted_string in anagrams_map:
                anagrams_map[sorted_string] += 1
            else:
                anagrams_map[sorted_string] = 1
    for count in anagrams_map.values():
        if count > 1:
            anagrams_count += count * (count - 1) // 2
    return anagrams_count >= 16