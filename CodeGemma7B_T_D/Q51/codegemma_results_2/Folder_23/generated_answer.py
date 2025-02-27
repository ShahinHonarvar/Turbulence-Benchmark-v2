from collections import defaultdict

def if_contains_anagrams(str_list):
    counts = defaultdict(int)
    for string in str_list:
        clean_string = ''.join((ch.lower() for ch in string if ch.isalpha()))
        sorted_string = ''.join(sorted(clean_string))
        counts[sorted_string] += 1
    if any((count > 49 for count in counts.values())):
        return False
    return True