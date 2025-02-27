from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            anagram_dict[sorted_str].append(string)
    anagram_count = 0
    for group in anagram_dict.values():
        if len(group) > 1:
            n = len(group)
            anagram_count += n * (n - 1) // 2
            if anagram_count >= 38:
                return True
    return False