from collections import defaultdict

def if_contains_anagrams(strings_list):
    if len(strings_list) <= 5:
        return True
    anagrams_counter = defaultdict(int)
    for string in strings_list:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        anagrams_counter[sorted_string] += 1
        if anagrams_counter[sorted_string] > 1:
            return True
    return False