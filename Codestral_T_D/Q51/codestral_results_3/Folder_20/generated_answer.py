from collections import Counter

def if_contains_anagrams(strings):
    anagram_counts = Counter()
    for string in strings:
        lower_string = string.lower()
        if len(lower_string) >= 3:
            sorted_string = ''.join(sorted(lower_string))
            anagram_counts[sorted_string] += 1
    return sum((count * (count - 1) for count in anagram_counts.values())) <= 131