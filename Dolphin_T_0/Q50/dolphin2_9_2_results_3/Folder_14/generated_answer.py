def if_contains_anagrams(strings):
    anagram_pairs = 0
    for string1 in strings:
        if len(string1) >= 3:
            lower_string1 = string1.lower()
            for string2 in strings:
                if string1 != string2 and len(string2) >= 3:
                    lower_string2 = string2.lower()
                    if sorted(lower_string1) == sorted(lower_string2):
                        anagram_pairs += 1
    return anagram_pairs >= 22