from collections import defaultdict

def if_contains_anagrams(strings):
    count_pairs = 0
    anagram_dict = defaultdict(int)
    for string in strings:
        normalized = ''.join(sorted([char.lower() for char in string if char.isalpha()]))
        if len(normalized) >= 3:
            anagram_dict[normalized] += 1
    for count in anagram_dict.values():
        if count > 1:
            count_pairs += count * (count - 1) // 2
            if count_pairs > 392:
                return False
    return True