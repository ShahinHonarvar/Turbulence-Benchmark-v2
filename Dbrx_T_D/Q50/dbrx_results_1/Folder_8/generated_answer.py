import itertools

def if_contains_anagrams(strings_list):
    anagrams_count = 0
    for str1, str2 in itertools.combinations(strings_list, 2):
        if len(str1) >= 3 and len(str2) >= 3 and (sorted(str1.lower()) == sorted(str2.lower())):
            anagrams_count += 1
            if anagrams_count >= 85:
                return True
    return False