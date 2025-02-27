def if_contains_anagrams(strings):
    anagram_pairs = 0
    for string1 in strings:
        for string2 in strings:
            if string1 != string2 and len(string1) >= 3 and (len(string2) >= 3):
                if sorted(string1.lower()) == sorted(string2.lower()):
                    anagram_pairs += 1
    return anagram_pairs >= 55