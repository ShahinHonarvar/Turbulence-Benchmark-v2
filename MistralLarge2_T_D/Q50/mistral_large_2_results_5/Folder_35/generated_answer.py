from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for s in strings:
        sorted_str = ''.join(sorted(s.lower()))
        anagram_dict[sorted_str].append(s)
    count = 0
    for key, value in anagram_dict.items():
        if len(value) >= 2 and len(key) >= 3:
            count += len(value) * (len(value) - 1) // 2
    return count >= 153