import re
from collections import Counter

def if_contains_anagrams(strings):
    anagrams = []
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(re.findall('[a-zA-Z]', string.lower())))
            anagrams.append(sorted_string)
    anagram_counts = Counter(anagrams)
    return sum((count * (count - 1) // 2 for count in anagram_counts.values())) <= 19