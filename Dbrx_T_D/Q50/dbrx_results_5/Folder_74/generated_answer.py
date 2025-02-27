import itertools

def if_contains_anagrams(string_list):
    anagrams_pairs = 0
    for string in string_list:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if string_list.count(sorted_string) > 1:
                anagrams_pairs += 1
    return anagrams_pairs >= 17