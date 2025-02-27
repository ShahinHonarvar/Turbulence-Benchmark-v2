import itertools

def if_contains_anagrams(string_list):
    anagram_counts = {}
    for string in string_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagram_counts[sorted_string] = anagram_counts.get(sorted_string, 0) + 1
    total_pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return total_pairs >= 49