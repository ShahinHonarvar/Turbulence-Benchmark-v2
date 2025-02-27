from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for s in strings:
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s.lower()))
        anagram_dict[sorted_str].append(s)
    count = 0
    for key in anagram_dict:
        if len(anagram_dict[key]) >= 2:
            count += 1
            if count > 26:
                return False
    return True