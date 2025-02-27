import itertools

def if_contains_anagrams(string_list):
    anagrams_count = 0
    for string1, string2 in itertools.combinations(string_list, 2):
        if len(string1) >= 3 and len(string2) >= 3 and (sorted(string1.lower()) == sorted(string2.lower())):
            anagrams_count += 1
            if anagrams_count >= 276:
                return True
    return False