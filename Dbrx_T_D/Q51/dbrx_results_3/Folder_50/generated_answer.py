import collections

def if_contains_anagrams(strings):
    anagrams = []
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagrams.append(sorted_string)
    anagram_counts = collections.Counter(anagrams)
    return sum((count * (count - 1) // 2 for count in anagram_counts.values())) <= 47