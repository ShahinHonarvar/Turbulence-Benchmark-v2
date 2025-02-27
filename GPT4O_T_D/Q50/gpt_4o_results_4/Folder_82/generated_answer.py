from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            anagram_dict[sorted_s] += 1
    count = 0
    for occurrences in anagram_dict.values():
        if occurrences > 1:
            count += occurrences * (occurrences - 1) // 2
        if count >= 276:
            return True
    return False