import difflib

def if_contains_anagrams(string_list):
    anagrams = []
    for string1 in string_list:
        for string2 in string_list:
            if difflib.SequenceMatcher(None, string1.lower(), string2.lower()).ratio() == 1 and string1 != string2 and (len(string1) >= 3) and (len(anagrams) < 40):
                anagrams.append((string1, string2))
    return len(anagrams) > 0