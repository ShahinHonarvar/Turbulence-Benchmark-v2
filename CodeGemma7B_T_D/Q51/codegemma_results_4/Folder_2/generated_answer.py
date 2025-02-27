from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(set)
    for s in str_list:
        chars = sorted([c.lower() for c in s if c.isalpha()])
        key = ''.join(chars)
        if len(key) >= 3:
            str_dict[key].add(s)
    count = 0
    for _, anagram_set in str_dict.items():
        count += len(anagram_set) * (len(anagram_set) - 1) // 2
    return count <= 81