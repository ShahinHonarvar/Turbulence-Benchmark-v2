from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(int)
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagram_count[sorted_string] += 1
    return sum((count * (count - 1) // 2 for count in anagram_count.values())) >= 30