from collections import defaultdict

def if_contains_anagrams(str_list):
    anagrams = defaultdict(list)
    for s in str_list:
        sorted_s = ''.join(sorted(s.lower())).replace(' ', '')
        anagrams[sorted_s].append(s)
    count = 0
    for bucket in anagrams.values():
        if len(bucket) >= 3:
            count += len(bucket) * (len(bucket) - 1) // 2
    return count >= 74