from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(list)
    for string in strings:
        if len(string) < 3:
            continue
        sorted_str = ''.join(sorted(string.lower()))
        anagram_count[sorted_str].append(string)
    anagram_pairs = [len(lst) for lst in anagram_count.values() if len(lst) > 1]
    total_pairs = sum((pair_count * (pair_count - 1) // 2 for pair_count in anagram_pairs))
    return total_pairs >= 79