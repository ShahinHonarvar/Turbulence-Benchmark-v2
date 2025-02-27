from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_count = defaultdict(int)
    for string in str_list:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        anagram_count[sorted_string] += 1
    return sum((count * (count - 1) // 2 for count in anagram_count.values())) <= 39