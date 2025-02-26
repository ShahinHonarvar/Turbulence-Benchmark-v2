from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_count = 0
    letter_count = defaultdict(list)
    for s in string_list:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            letter_count[sorted_s].append(s)
    for group in letter_count.values():
        n = len(group)
        if n > 1:
            anagram_count += n * (n - 1) // 2
    return anagram_count >= 48