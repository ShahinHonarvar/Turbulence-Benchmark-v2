from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = 0
    seen = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            normalized = ''.join(sorted(string.lower()))
            seen[normalized] += 1
    for count in seen.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
            if anagram_count > 93:
                return False
    return anagram_count <= 93