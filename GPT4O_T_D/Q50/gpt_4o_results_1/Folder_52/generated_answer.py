from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            key = ''.join(sorted(s.lower()))
            anagram_dict[key].append(s)
    count = 0
    for anagrams in anagram_dict.values():
        n = len(anagrams)
        if n > 1:
            count += n * (n - 1) // 2
    return count >= 58