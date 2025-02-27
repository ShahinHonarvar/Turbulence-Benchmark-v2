from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = 0
    anagrams = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            anagrams[sorted_str].append(string)
    for group in anagrams.values():
        n = len(group)
        if n > 1:
            anagram_count += n * (n - 1) // 2
        if anagram_count >= 91:
            return True
    return anagram_count >= 91