from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    anagrams_count = defaultdict(int)
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    for string in list_of_strings:
        string_lower = string.lower()
        string_filtered = ''.join(filter(lambda x: x in english_letters, string_lower))
        if len(string_filtered) < 3:
            continue
        sorted_string = ''.join(sorted(string_filtered))
        anagrams_count[sorted_string] += 1
    pairs_count = sum((count * (count - 1) // 2 for count in anagrams_count.values()))
    return pairs_count <= 8