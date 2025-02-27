from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams_count = defaultdict(int)
    for string in lst:
        string = ''.join(filter(str.isalpha, string)).lower()
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string))
        anagrams_count[sorted_string] += 1
    return sum((count * (count - 1) // 2 for count in anagrams_count.values())) <= 257