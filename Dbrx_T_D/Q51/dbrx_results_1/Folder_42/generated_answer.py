import collections

def if_contains_anagrams(string_list):
    anagram_count = 0
    for string1 in string_list:
        for string2 in string_list:
            if string1 == string2:
                continue
            string1 = string1.lower()
            string2 = string2.lower()
            if len(string1) < 3 or len(string2) < 3:
                continue
            if collections.Counter(string1) == collections.Counter(string2):
                anagram_count += 1
                if anagram_count > 38:
                    return False
    return True