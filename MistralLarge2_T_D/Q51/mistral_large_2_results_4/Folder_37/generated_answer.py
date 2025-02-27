from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1) == sorted(str2)
    anagram_count = defaultdict(int)
    for string in strings:
        if len(string) < 3:
            continue
        sorted_str = ''.join(sorted(string.lower()))
        anagram_count[sorted_str] += 1
    total_pairs = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return total_pairs <= 206