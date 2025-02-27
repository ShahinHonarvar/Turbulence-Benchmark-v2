import itertools

def if_contains_anagrams(strings):
    anagrams_count = 0
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            for compare_string in strings:
                if len(compare_string) >= 3 and string != compare_string:
                    sorted_compare_string = ''.join(sorted(compare_string.lower()))
                    if sorted_string == sorted_compare_string:
                        anagrams_count += 1
    return anagrams_count >= 48