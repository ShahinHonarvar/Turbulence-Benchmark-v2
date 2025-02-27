import itertools

def if_contains_anagrams(string_list):
    anagrams_count = 0
    for string1, string2 in itertools.combinations(string_list, 2):
        string1 = ''.join(sorted(string1.lower()))
        string2 = ''.join(sorted(string2.lower()))
        if len(string1) >= 3 and string1 == string2:
            anagrams_count += 1
        if anagrams_count >= 42:
            return True
    return False