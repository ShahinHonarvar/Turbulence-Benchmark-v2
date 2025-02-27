from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(list)
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        anagram_count[sorted_string].append(string)
    count = 0
    for key in anagram_count:
        if len(anagram_count[key]) > 1:
            count += len(anagram_count[key]) // 2
    return count >= 8