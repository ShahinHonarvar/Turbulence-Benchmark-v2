def if_contains_anagrams(strings):
    for string1 in strings:
        for string2 in strings:
            if string1 != string2 and len(string1) >= 3 and (len(string2) >= 3):
                string1 = string1.lower()
                string2 = string2.lower()
                if sorted(string1) == sorted(string2):
                    return True
    return False