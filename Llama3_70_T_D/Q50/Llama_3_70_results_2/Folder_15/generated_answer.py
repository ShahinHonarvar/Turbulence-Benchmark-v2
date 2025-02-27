from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for string in lst:
        lower_string = string.lower()
        if len(lower_string) >= 3:
            sorted_string = ''.join(sorted(lower_string))
            anagrams[sorted_string].append(lower_string)
    count = sum((1 for v in anagrams.values() if len(v) > 1))
    return count >= 4