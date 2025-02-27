from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_dict = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            anagram_dict[sorted_str].append(string)
    for anagram_list in anagram_dict.values():
        n = len(anagram_list)
        if n > 1:
            anagram_count += n * (n - 1) // 2
            if anagram_count > 67:
                return False
    return True