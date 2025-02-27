from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = 0
    normalized_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    anagram_groups = defaultdict(int)
    for ns in normalized_strings:
        anagram_groups[ns] += 1
    for count in anagram_groups.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
            if anagram_count > 67:
                return False
    return True