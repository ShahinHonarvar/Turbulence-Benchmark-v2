from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = 0
    grouped_anagrams = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            grouped_anagrams[sorted_string] += 1
    for count in grouped_anagrams.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
    return anagram_count >= 86