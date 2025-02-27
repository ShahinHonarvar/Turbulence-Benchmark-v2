from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams_count = 0
    seen = defaultdict(int)
    for string in strings:
        if len(string) < 3:
            continue
        sorted_str = ''.join(sorted(string.lower()))
        seen[sorted_str] += 1
    for count in seen.values():
        if count > 1:
            anagrams_count += count * (count - 1) // 2
    return anagrams_count <= 34