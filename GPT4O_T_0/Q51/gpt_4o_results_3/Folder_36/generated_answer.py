from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = 0
    normalized_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    anagram_dict = defaultdict(int)
    for ns in normalized_strings:
        anagram_dict[ns] += 1
    for count in anagram_dict.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
            if anagram_count > 25:
                return False
    return True