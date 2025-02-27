from collections import Counter

def if_contains_anagrams(str_list):
    anagram_counts = Counter()
    for str1 in str_list:
        str1 = ''.join(sorted(str1.lower()))
        if len(str1) < 3:
            continue
        anagram_counts[str1] += 1
    num_pairs = 0
    for count in anagram_counts.values():
        num_pairs += count * (count - 1) // 2
    return num_pairs <= 20