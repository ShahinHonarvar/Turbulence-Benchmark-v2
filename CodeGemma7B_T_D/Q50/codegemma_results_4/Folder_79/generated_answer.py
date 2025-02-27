def if_contains_anagrams(list_of_strings):
    anagrams = {}
    for string in list_of_strings:
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string not in anagrams:
            anagrams[sorted_string] = []
        anagrams[sorted_string].append(string)
    count = 0
    for anagram_list in anagrams.values():
        if len(anagram_list) >= 3:
            count += len(anagram_list) - 2
    return count >= 40