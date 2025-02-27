from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(list)
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(sorted_s) >= 3:
            anagram_count[sorted_s].append(s)
    count = 0
    for key in anagram_count:
        n = len(anagram_count[key])
        if n > 1:
            count += n * (n - 1) // 2
    return count <= 85