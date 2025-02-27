from collections import defaultdict

def if_contains_anagrams(string_list):
    anagrams_count = defaultdict(int)
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    for string_ in string_list:
        sorted_string = ''.join(sorted(filter(lambda x: x.lower() in english_letters, string_))).lower()
        if len(sorted_string) >= 3:
            anagrams_count[sorted_string] += 1
    return sum(anagrams_count.values()) <= 276