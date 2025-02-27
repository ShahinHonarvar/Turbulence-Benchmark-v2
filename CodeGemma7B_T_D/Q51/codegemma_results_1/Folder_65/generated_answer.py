from collections import defaultdict

def if_contains_anagrams(str_list):
    dict_count = defaultdict(int)
    for string in str_list:
        sorted_str = ''.join(sorted(string.lower()))
        if len(sorted_str) >= 3:
            dict_count[sorted_str] += 1
    sorted_counts = sorted(dict_count.values(), reverse=True)
    total_pairs = 0
    for count in sorted_counts:
        total_pairs += count * (count - 1) // 2
    return total_pairs <= 72