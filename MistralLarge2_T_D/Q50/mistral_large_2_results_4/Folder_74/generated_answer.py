from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    count = 0
    for s in strings:
        if len(s) < 3:
            continue
        key = ''.join(sorted(s.lower()))
        anagram_dict[key].append(s)
    for key in anagram_dict:
        if len(anagram_dict[key]) > 1:
            count += len(anagram_dict[key]) - 1
    return count >= 17