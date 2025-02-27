def if_contains_anagrams(str_list):
    anagram_sets = {}
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in anagram_sets:
            anagram_sets[sorted_string].add(string)
        else:
            anagram_sets[sorted_string] = {string}
    num_sets = len(anagram_sets)
    return num_sets <= 70