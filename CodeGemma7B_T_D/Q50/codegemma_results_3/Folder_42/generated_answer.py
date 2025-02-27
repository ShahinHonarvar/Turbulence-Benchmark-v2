from collections import defaultdict

def if_contains_anagrams(str_list):
    anagrams = defaultdict(list)
    for s in str_list:
        if len(s) < 3:
            continue
        key = ''.join(sorted(s.lower()))
        anagrams[key].append(s)
    return len(anagrams) >= 233