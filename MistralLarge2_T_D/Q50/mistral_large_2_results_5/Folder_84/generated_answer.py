from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(int)
    count = 0
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        anagram_count[sorted_string] += 1
    for key in anagram_count:
        if anagram_count[key] > 1:
            count += anagram_count[key] * (anagram_count[key] - 1) // 2
    return count >= 108