def if_contains_anagrams(list_of_strings):
    anagram_pairs = 0
    for string1 in list_of_strings:
        if len(string1) < 3:
            continue
        sorted_string1 = ''.join(sorted(string1.lower()))
        for string2 in list_of_strings:
            if string1 == string2 or len(string2) < 3:
                continue
            sorted_string2 = ''.join(sorted(string2.lower()))
            if sorted_string1 == sorted_string2:
                anagram_pairs += 1
    return anagram_pairs >= 98 * 99 // 2