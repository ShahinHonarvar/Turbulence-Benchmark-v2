from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_count = defaultdict(int)
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagram_count[sorted_string] += 1
    return sum((count > 1 for count in anagram_count.values())) <= 14