def if_contains_anagrams(list_of_strings):
    anagrams = {}
    anagram_pairs = 0
    for string in list_of_strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in anagrams:
            anagrams[sorted_string] += 1
            if anagrams[sorted_string] == 2:
                anagram_pairs += 1
        else:
            anagrams[sorted_string] = 1
    return anagram_pairs >= 11