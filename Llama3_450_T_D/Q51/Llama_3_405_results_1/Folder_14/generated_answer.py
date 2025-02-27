from collections import defaultdict

def if_contains_anagrams(string_list):
    anagrams = defaultdict(list)
    for s in string_list:
        if len(s) >= 3 and s.isalpha():
            sorted_str = ''.join(sorted(s.lower()))
            anagrams[sorted_str].append(s)
    count = 0
    for v in anagrams.values():
        count += len(v) * (len(v) - 1) // 2
        if count > 474:
            return False
    return True