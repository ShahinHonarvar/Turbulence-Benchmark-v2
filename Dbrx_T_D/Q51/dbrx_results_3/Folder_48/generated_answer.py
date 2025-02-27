import itertools

def if_contains_anagrams(strings_list):
    anagrams_count = 0
    for string1, string2 in itertools.combinations(strings_list, 2):
        if len(string1) >= 3 and len(string2) >= 3 and (sorted(string1.lower()) == sorted(string2.lower())) and (anagrams_count < 277):
            anagrams_count += 1
        elif anagrams_count >= 277:
            return False
    return anagrams_count <= 277