import itertools

def if_contains_anagrams(strings_list):
    anagrams_count = 0
    for str_len in range(3, len(max(strings_list, key=len)) + 1):
        strings_of_specific_len = [s.lower() for s in strings_list if len(s) == str_len]
        for pair in itertools.combinations(strings_of_specific_len, 2):
            if sorted(pair[0]) == sorted(pair[1]):
                anagrams_count += 1
                if anagrams_count >= 97:
                    return True
    return False