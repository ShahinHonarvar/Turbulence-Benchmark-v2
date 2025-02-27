from collections import defaultdict

def if_contains_anagrams(str_list):
    char_counts = defaultdict(int)
    for string in str_list:
        if len(string) < 3:
            continue
        sorted_str = ''.join(sorted(string.lower()))
        char_counts[sorted_str] += 1
    count = 0
    for count in char_counts.values():
        count += (count - 1) // 2
    return count <= 47