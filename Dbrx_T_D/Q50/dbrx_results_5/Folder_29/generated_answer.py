from collections import Counter

def if_contains_anagrams(string_list):
    anagrams_counter = 0
    for string1 in string_list:
        string1 = string1.lower()
        if len(string1) < 3:
            continue
        sorted_string1 = ''.join(sorted(string1))
        anagram_pairs = [string1, sorted_string1]
        for string2 in string_list:
            if string2 in anagram_pairs:
                continue
            string2 = string2.lower()
            if len(string2) < 3:
                continue
            sorted_string2 = ''.join(sorted(string2))
            if sorted_string1 == sorted_string2 and string1 != string2:
                anagrams_counter += 1
                anagram_pairs.append(string2)
    return anagrams_counter >= 35