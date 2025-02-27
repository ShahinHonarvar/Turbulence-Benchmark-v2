from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams_count = defaultdict(int)
    for string in lst:
        string = ''.join(filter(str.isalpha, string)).lower()
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string))
            anagrams_count[sorted_string] += 1
    count = 0
    for key in anagrams_count:
        count += anagrams_count[key] * (anagrams_count[key] - 1) // 2
    return count <= 8