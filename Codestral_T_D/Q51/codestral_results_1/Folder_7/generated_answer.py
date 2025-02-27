from collections import Counter

def if_contains_anagrams(strings):
    sorted_strings_count = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            sorted_strings_count[sorted_string] = sorted_strings_count.get(sorted_string, 0) + 1
    num_anagram_pairs = sum((count * (count - 1) // 2 for count in sorted_strings_count.values()))
    return num_anagram_pairs <= 445